�摜�Í�

�J����
macOS HighSierra version:10.13.6 
Python3.7.0
openCV 4.0.0.21
opencv-contrib-python 4.1.2.30
numpy 1.17.4
Pillow 6.2.1

[ �T�v ]
�摜�����̂��׋������˂��v���O�����B
����͉摜��؂�\�肵�Ă�����x�Ȃ̂ŁA�����P���ȃA���S���Y���ł���B
�ڕW�Ƃ��Ă͈Í��������t�@�C���̃T�C�Y�����󌳂̃t�@�C���̓�{�Ȃ̂ŁA�Í����E�����������摜�f�[�^�̃T�C�Y�̏k���B
�܂��A����sharefile�Ƃ����Í��������t�@�C���̌�����ł��邪�A�ϐ��ɂ����Ă݂����B
�Ō��openCV��Pillow�̈̑傳�Ɋ��ӂ����B

[ �g���� ]
�����삳����ۂɊ��ɂ���Ă�numpy��openCV��Pillow�̃p�b�P�[�W���C���X�g�[������K�v������B

**�Í����̏ꍇ**
	�Í����������摜��p�ӂ��A�R�}���h���C�������Ɏw�肵�A���s
	```
	$python3 image_encoder.py filename
	```
	
		filename��"secret.png"�̏ꍇ�ɂ�
	```
	$python3 image_encoder.py secret.png
	```
	
	�o�͂����"share1.png", "share2.png"���Í������ꂽ�摜�B
	
**�������̏ꍇ**	
	�������������摜��񖇗p�ӂ��A�R�}���h���C�������Ɏw�肵�A���s
	```
	$python3 image_encoder.py filename1 filename2
	```
	
		filename1��"share1.png"�ƁAfilename2��"share2.png"�̏ꍇ�ɂ́A
	```
	$python3 image_encoder.py secret.png
	```
	
	�o�͂����"DecryptImage.png"�����������ꂽ�摜�B
	