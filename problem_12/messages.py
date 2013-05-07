import pymqi

qmgr = pymqi.connect('QM.1', 'SVRCONN.CHANNEL.1', '192.168.1.121(1434)')

getq = pymqi.Queue(qmgr, 'TESTQ.1')
print("Here's the message:", getq.get())
