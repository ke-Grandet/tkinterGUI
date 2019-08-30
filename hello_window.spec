# -*- mode: python -*-

block_cipher = None


a = Analysis(['hello_window.py'],
             pathex=['/myFrame/frame_direction.py', '/myFrame/frame_direction_char.py', '/myFrame/frame_message.py', '/myFrame/frame_show.py', '/myFrame/frame_size.py', '/myFrame/frame_special_char.py', '/myFrame/frame_start_point.py', '/src/button_rasengan.py', '/src/hello.py', 'F:\\PycharmProjects\\untitled'],
             binaries=[],
             datas=[],
             hiddenimports=['frame_direction', 'frame_direction_char', 'frame_message', 'frame_show', 'frame_size', 'frame_special_char', 'frame_start_point', 'button_rasengan', 'hello'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='hello_window',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
