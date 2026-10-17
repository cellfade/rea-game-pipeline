import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('pipeline', Path(__file__).resolve().parents[1] / 'harness/pipeline.py')
p = importlib.util.module_from_spec(spec); spec.loader.exec_module(p)

def project():
    return {'schema_version': 1, 'max_workers': 2, 'release_tasks': ['build'], 'tasks': [{'id': 'build', 'depends_on': [], 'allowed_files': ['src'], 'resources': [], 'status': 'done', 'revision': 'a'*64, 'author': 'builder', 'required_tests': ['behavior'], 'evidence_ids': ['rule']}], 'receipts': [{'task_id':'build','test':'behavior','status':'pass','revision':'a'*64}], 'reviews':[{'task_id':'build','author':'builder','reviewer':'reviewer','subject_digest':'a'*64,'verdict':'pass'}], 'evidence':[{'id':'rule','claim':'A measured rule','status':'observed','source':{'identity':'fixture-v1','locator':'frame 12'},'verified':True,'reviewer':'reviewer'}], 'uat':[{'task_id':'build','revision':'a'*64,'status':'pass','reviewer':'human'}]}

class Checks(unittest.TestCase):
    def test_alias_path_rejected(self):
        x=project(); x['tasks'][0]['allowed_files']=['./src/file']; self.assertTrue(p.validate(x))
    def test_control_path_rejected(self):
        x=project(); x['tasks'][0]['allowed_files']=['src'+chr(10)+'file']; self.assertTrue(p.validate(x))
    def test_later_failed_review_blocks(self):
        x=project(); r=copy.deepcopy(x['reviews'][0]); r['verdict']='fail'; x['reviews'].append(r); self.assertTrue(p.audit(x,'prototype'))
    def test_later_failed_uat_blocks(self):
        x=project(); r=copy.deepcopy(x['uat'][0]); r['status']='fail'; x['uat'].append(r); self.assertTrue(p.audit(x,'reference'))
    def test_active_requires_done_dependency(self):
        x=project(); a=x['tasks'][0]; a['status']='planned'; b=copy.deepcopy(a); b.update(id='dependent',status='active',depends_on=['build'],allowed_files=['other']); x['tasks'].append(b); self.assertTrue(p.validate(x))
    def test_duplicate_evidence_rejected(self):
        x=project(); x['evidence'].append(copy.deepcopy(x['evidence'][0])); self.assertTrue(p.validate(x))
    def test_malformed_collections_are_errors(self):
        for key,value in [('reviews',None),('receipts',[None]),('uat','bad'),('evidence',[{'source':[]}])]:
            x=project(); x[key]=value; self.assertTrue(p.validate(x)); self.assertTrue(p.audit(x,'reference'))
    def test_independent_evidence_and_uat(self):
        for key in ('evidence','uat'):
            x=project(); x[key][0]['reviewer']='builder'; self.assertTrue(p.audit(x,'reference'))
    def test_reference_pass(self): self.assertEqual(p.audit(project(), 'reference'), [])
    def test_empty_fails(self):
        x=project(); x['tasks']=[]; x['release_tasks']=[]
        self.assertTrue(p.audit(x,'prototype'))
    def test_planned_release_fails(self):
        x=project(); x['tasks'][0]['status']='planned'; self.assertTrue(p.audit(x,'prototype'))
    def test_stale_receipt_fails(self):
        x=project(); x['receipts'][0]['revision']='b'*64; self.assertTrue(p.audit(x,'prototype'))
    def test_self_review_fails(self):
        x=project(); x['reviews'][0]['reviewer']='builder'; self.assertTrue(p.audit(x,'prototype'))
    def test_wrong_review_digest_fails(self):
        x=project(); x['reviews'][0]['subject_digest']='b'*64; self.assertTrue(p.audit(x,'prototype'))
    def test_linked_evidence_required(self):
        x=project(); x['tasks'][0]['evidence_ids']=['missing']; self.assertTrue(p.audit(x,'reference'))
    def test_uat_separate(self):
        x=project(); x['uat']=[]; self.assertEqual(p.audit(x,'prototype'),[]); self.assertTrue(p.audit(x,'reference'))
    def test_traversal(self):
        for path in ('../escape','/absolute','C:/absolute','safe/../../escape'):
            x=project(); x['tasks'][0]['allowed_files']=[path]; self.assertTrue(p.validate(x))
    def test_cycle(self):
        x=project(); x['tasks'][0]['depends_on']=['build']; self.assertTrue(p.validate(x))
    def test_active_lock_and_capacity(self):
        x=project(); a=x['tasks'][0]; a['status']='active'
        b=copy.deepcopy(a); b.update(id='other',status='planned',allowed_files=['src/file']); x['tasks'].append(b)
        self.assertEqual(p.ready(x),[])
        b['allowed_files']=['docs']; self.assertEqual(p.ready(x),['other'])
        x['max_workers']=1; self.assertEqual(p.ready(x),[])
    def test_resource_conflict(self):
        a=project()['tasks'][0]; b=copy.deepcopy(a); a['resources']=['scene']; b['resources']=['scene']; b['allowed_files']=['other']; self.assertTrue(p.conflict(a,b))
    def test_privacy_redacts(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root,'sample.txt').write_text('/'+'Users/'+'fixture'+'/file')
            findings=p.privacy(root); self.assertTrue(findings); self.assertNotIn('fixture',str(findings))
    def test_binary_manual_review(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root,'asset.bin').write_bytes(bytes([255,254])); self.assertTrue(p.privacy(root))

if __name__=='__main__': unittest.main()
