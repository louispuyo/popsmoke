from pyroute2 import NDB

ndb = NDB(log='on')
for record in ndb.interfaces.summary():
    print(record.ifname, record.address, record.state)

for record in ndb.addresses.summary():
    print(record._as_dict())

(ndb
 .interfaces
 .create(ifname='br1', kind='bridge')  # create a bridge
 .add_port('eth0')                     # add ports
 .add_port('eth1')                     #
 .add_ip('10.0.0.1/24')                # add addresses
 .add_ip('192.168.0.1/24')             #
 .set('br_stp_state', 1)               # set STP on
 .set('state', 'up')                   # bring the interface up
 .commit())                    
