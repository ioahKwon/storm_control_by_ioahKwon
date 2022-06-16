set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%

call conda env list
call conda activate py36
call cd C:\git\storm-control-kimlab\storm_control\hal4000\
call python hal4000.py xml/STORM.xml

pause