import angr
p = angr.Project(r'E:\Learn\Python\BUUCTF\Reverese\signal.exe')
st = p.factory.entry_state()
sm = p.factory.simulation_manager(st)
sm.explore(find=0x40175E, avoid=0x4016E6)
print(sm.found[0].posix.dumps(0))