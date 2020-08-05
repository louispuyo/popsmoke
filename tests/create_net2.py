from socket import AF_INET
from pyroute2 import IPRoute

# get access to the netlink socket
ip = IPRoute()
# no monitoring here -- thus no bind()

# print interfaces
for link in ip.get_links():
    print(link)

# create VETH pair and move v0p1 to netns 'test'
ip.link('add', ifname='v0p0', peer='v0p1', kind='veth')
idx = ip.link_lookup(ifname='v0p1')[0]
ip.link('set', index=idx, net_ns_fd='test')

# bring v0p0 up and add an address
idx = ip.link_lookup(ifname='v0p0')[0]
ip.link('set', index=idx, state='up')
ip.addr('add', index=idx, address='10.0.0.1', prefixlen=24)

# release Netlink socket
ip.close()