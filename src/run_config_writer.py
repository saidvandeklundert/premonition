# for every configuration file in test date, create a corresponding token file.
from juniper.configwriter import ConfigWriter
from juniper.lexer import Lexer
import glob
from pathlib import Path
import logging
import pprint

logging.basicConfig(level=logging.INFO)
import json

original = """version 17.2R3.4;
system {
    login {
        class READ {
            permissions [ clear maintenance network reset trace view view-configuration ];
        }
        user engineer {
            uid 2999;
            class super-user;
            authentication {
                encrypted-password /* SECRET-DATA */; ## SECRET-DATA
            }
        }
        user noc-auto {
            uid 4001;
            class super-user;
            authentication {
                encrypted-password /* SECRET-DATA */; ## SECRET-DATA
            }
        }
        user noc-write {
            uid 4002;                   
            class super-user;
            authentication {
                encrypted-password /* SECRET-DATA */; ## SECRET-DATA
            }
        }
        user noc-read {
            uid 4003;
            class READ;
            authentication {
                encrypted-password /* SECRET-DATA */; ## SECRET-DATA
            }
        }
    }
    root-authentication {
        encrypted-password /* SECRET-DATA */; ## SECRET-DATA
    }
    host-name dar01-dal09;
    domain-name example.com;
    time-zone UTC;
    no-redirects;
    arp {
        aging-timer 5;
    }                                   
    internet-options {
        path-mtu-discovery;
    }
    authentication-order password;
    name-server {
        12.12.1.222;
        12.12.1.220;
    }
    services {
        ftp;
        ssh;
        netconf {
            ssh {
                port 830;
            }
        }
    }
    syslog {
        archive size 100k;
        user * {
            any emergency;
        }
        host 10.1.1.1 {             
            any notice;
        }
        host 10.1.1.2 {
            any notice;
        }
        file messages {
            any any;
            authorization none;
            interactive-commands none;
            match "!(.*not Juniper supported SFP.*|(.*Input IFL not found.*))";
            explicit-priority;
        }
        file interactive-commands {
            interactive-commands any;
            explicit-priority;
        }
        file login-attempts {           
            authorization any;
            explicit-priority;
        }
        source-address 10.200.1.1;
    }
    ntp {
        server 192.1.1.1;
        server 192.1.1.2;
        server 192.1.1.3;
        server 192.1.1.4;
        server 192.1.1.5;
        server 192.1.1.6;
        server 192.1.1.7;
        server 192.1.1.8;
        server 192.1.1.9;
        server 192.1.1.10;
        server 192.1.1.11;
        server 192.1.1.12;
        source-address 10.200.1.1;
    }
}
chassis {
    aggregated-devices {                
        ethernet {
            device-count 40;
        }
    }
}
interfaces {
    ge-0/0/0 {
        description "LACP 1 TO SW1";
        ether-options {
            802.3ad ae1;
        }
    }
    ge-0/0/1 {
        description "LACP 2 TO SW2";
        ether-options {
            802.3ad ae2;
        }
    }
    ge-0/0/2 {
        description "LACP 3 TO SW3";
        ether-options {
            802.3ad ae3;
        }                               
    }
    ge-0/0/3 {
        description "LACP 4 TO SW4";
        ether-options {
            802.3ad ae4;
        }
    }
    ge-0/0/4 {
        description "LACP 5 TO SW5";
        ether-options {
            802.3ad ae5;
        }
    }
    ge-0/0/5 {
        description "LACP 6 TO SW6";
        ether-options {
            802.3ad ae6;
        }
    }
    ge-0/0/6 {
        description "UNUSED";
        unit 0 {
            family inet;                
        }
    }
    ge-0/0/7 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/8 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/9 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/10 {
        description "UNUSED";
        unit 0 {                        
            family inet;
        }
    }
    ge-0/0/11 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/12 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/13 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/14 {
        description "UNUSED"; 
        unit 0 {
            family inet;
        }
    }
    ge-0/0/15 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/16 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/17 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/18 {                         
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/19 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/20 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/21 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }                                   
    ge-0/0/22 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/23 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/24 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/25 {
        description "UNUSED";
        unit 0 {
            family inet;
        }                               
    }
    ge-0/0/26 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/27 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    ge-0/0/28 {
        description "LACP 101 TO TOR1";
        ether-options {
            802.3ad ae101;
        }
    }
    ge-0/0/29 {
        description "LACP 102 TO TOR2";
        ether-options {
            802.3ad ae102;              
        }
    }
    ge-0/0/30 {
        description "LACP 201 TO FW";
        ether-options {
            802.3ad ae201;
        }
    }
    ge-0/0/31 {
        description "LACP 202 TO FW";
        ether-options {
            802.3ad ae202;
        }
    }
    xe-0/0/32 {
        description "UNUSED";
        unit 0 {
            family inet;
        }
    }
    xe-0/0/33 {
        description "UNUSED";
        unit 0 {                        
            family inet;
        }
    }
    xe-0/0/34 {
        description "TO BASEMENT";
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN310 VLAN703 VLAN704 ];
                }
            }
        }
    }
    xe-0/0/35 {
        description "LACP 111 linking to TO BR SW1";
        ether-options {
            802.3ad ae111;
        }
    }
    ae1 {
        description "Interfaces [ge-0/0/0] TO ISW1";
        aggregated-ether-options {      
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }
            }
        }
    }                                   
    ae2 {
        description "Interfaces [ge-0/0/1] TO ISW2";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }                       
            }
        }
    }
    ae3 {
        description "Interfaces [ge-0/0/2] TO ISW3";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }
            }
        }
    }
    ae4 {
        description "Interfaces [ge-0/0/3] TO ISW4";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }
            }
        }
    }
    ae5 {
        description "Interfaces [ge-0/0/4] TO ISW5";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching { 
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }
            }
        }
    }
    ae6 {
        description "Interfaces [ge-0/0/5] TO ISW6";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }                           
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }
            }
        }
    }
    ae101 {
        description "Interfaces [ge-0/0/28] TO ACC SW1";
        aggregated-ether-options {
            lacp {                      
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }
            }
        }
    }
    ae102 {                             
        description "Interfaces [ge-0/0/29] TO ACC SW2";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members [ VLAN101 VLAN102 VLAN103 VLAN110 VLAN684 VLAN310 VLAN699 VLAN698 VLAN702 VLAN703 VLAN704 VLAN705 VLAN706 VLAN708 VLAN709 VLAN710 VLAN711 VLAN712 VLAN713 VLAN740 VLAN741 VLAN800 VLAN801 VLAN802 VLAN811 VLAN812 VLAN813 VLAN814 VLAN815 VLAN816 VLAN817 VLAN818 VLAN819 VLAN820 VLAN821 VLAN822 VLAN823 VLAN826 VLAN827 VLAN828 VLAN829 VLAN830 VLAN831 VLAN835 VLAN839 VLAN840 VLAN843 VLAN844 VLAN848 VLAN845 VLAN846 VLAN850 VLAN847 VLAN849 VLAN851 VLAN836 VLAN837 VLAN899 VLAN900 VLAN912 VLAN999 VLAN841 VLAN842 
                    VLAN833 VLAN854 VLAN855 VLAN856 VLAN857 VLAN858 VLAN859 VLAN860 VLAN891 VLAN892 VLAN893 VLAN895 VLAN852 VLAN894 VLAN861 VLAN862 VLAN865 VLAN866 VLAN867 VLAN863 VLAN898 VLAN890 ];
                }
            }                           
        }
    }
    ae111 {
        description "Interfaces [xe-0/0/35] to TO BR SW1";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members all;
                }
            }
        }
    }
    ae201 {
        description "Interfaces [ge-0/0/30] to BR FW1";
        aggregated-ether-options {
            lacp {                      
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching {
                interface-mode trunk;
                vlan {
                    members all;
                }
            }
        }
    }
    ae202 {
        description "Interfaces [ge-0/0/31] to BR FW2";
        aggregated-ether-options {
            lacp {
                active;
                periodic slow;
            }
        }
        unit 0 {
            family ethernet-switching { 
                interface-mode trunk;
                vlan {
                    members all;
                }
            }
        }
    }
    irb {
        description "mgmt";
        unit 698 {
            family inet {
                address 10.200.1.1/22;
            }
        }
    }
    vme {
        description "oob";
        unit 0 {
            family inet {
                address 10.30.0.22/8;
            }
        }
    }                                   
}
snmp {
    location DAL09;
    v3 {
        usm {
            local-engine {
                user POLLER-1 {
                    authentication-sha {
                        authentication-key /* SECRET-DATA */; ## SECRET-DATA
                    }
                    privacy-aes128 {
                        privacy-key /* SECRET-DATA */; ## SECRET-DATA
                    }
                }
                user POLLER-2 {
                    authentication-sha {
                        authentication-key /* SECRET-DATA */; ## SECRET-DATA
                    }
                    privacy-aes128 {
                        privacy-key /* SECRET-DATA */; ## SECRET-DATA
                    }
                }
            }                           
        }
        vacm {
            security-to-group {
                security-model usm {
                    security-name POLLER-1 {
                        group view-all;
                    }
                    security-name POLLER-2 {
                        group view-all;
                    }
                }
            }
            access {
                group view-all {
                    default-context-prefix {
                        security-model usm {
                            security-level privacy {
                                read-view view-all;
                            }
                        }
                    }
                }
            }                           
        }
    }
    engine-id {
        local dar01-dal09;
    }
    view view-all {
        oid .1 include;
    }
}
forwarding-options {
    storm-control-profiles default {
        all;
    }
}
routing-options {
    static {
        route 0.0.0.0/0 next-hop 10.0.0.1;
        route 1.0.0.0/16 next-hop 2.0.0.254;
        route 1.31.0.0/16 next-hop 2.0.0.254;
    }
}
protocols {
    lldp {                              
        port-description-type interface-description;
        interface all;
        interface me0 {
            disable;
        }
    }
    lldp-med {
        interface all;
        interface me0 {
            disable;
        }
    }
    mstp {
        bridge-priority 8k;
        bpdu-block-on-edge;
        interface xe-0/0/34;
        interface ae1;
        interface ae2;
        interface ae3;
        interface ae4;
        interface ae5;
        interface ae6;
        interface ae101;                
        interface ae102;
        interface ae111;
        interface ae201;
        interface ae202;
    }
}
poe {
    interface all;
}
vlans {
    VLAN101 {
        vlan-id 101;
    }
    VLAN102 {
        vlan-id 102;
    }
    VLAN103 {
        vlan-id 103;
    }
    VLAN110 {
        vlan-id 110;
    }
    VLAN310 {                    
        vlan-id 310;
    }
    VLAN684 {
        vlan-id 684;
    }
    VLAN697 {
        vlan-id 697;
    }
    VLAN698 {
        vlan-id 698;
        l3-interface irb.698;
    }    
    VLAN699 {
        vlan-id 699;
    }
    VLAN702 {
        vlan-id 702;
    }
    VLAN703 {
        vlan-id 703;
    }
    VLAN704 {
        vlan-id 704;                    
    }
    VLAN705 {
        vlan-id 705;
    }
    VLAN706 {
        vlan-id 706;
    }
    VLAN708 {
        vlan-id 708;
    }
    VLAN709 {
        vlan-id 709;
    }
    VLAN710 {
        vlan-id 710;
    }
    VLAN711 {
        vlan-id 711;
    }
    VLAN712 {
        vlan-id 712;
    }
    VLAN713 {                           
        vlan-id 713;
    }
    VLAN740 {
        vlan-id 740;
    }
    VLAN741 {
        vlan-id 741;
    }
    VLAN800 {
        vlan-id 800;
    }
    VLAN801 {
        vlan-id 801;
    }
    VLAN802 {
        vlan-id 802;
    }
    VLAN811 {
        vlan-id 811;
    }
    VLAN812 {
        vlan-id 812;
    }                                   
    VLAN813 {
        vlan-id 813;
    }
    VLAN814 {
        vlan-id 814;
    }
    VLAN815 {
        vlan-id 815;
    }
    VLAN816 {
        vlan-id 816;
    }
    VLAN817 {
        vlan-id 817;
    }
    VLAN818 {
        vlan-id 818;
    }
    VLAN819 {
        vlan-id 819;
    }
    VLAN820 {
        vlan-id 820;                    
    }
    VLAN821 {
        vlan-id 821;
    }
    VLAN822 {
        vlan-id 822;
    }
    VLAN823 {
        vlan-id 823;
    }
    VLAN824 {
        vlan-id 824;
    }
    VLAN826 {
        vlan-id 826;
    }
    VLAN827 {
        vlan-id 827;
    }
    VLAN828 {
        vlan-id 828;
    }
    VLAN829 {                           
        vlan-id 829;
    }
    VLAN830 {
        vlan-id 830;
    }
    VLAN831 {
        vlan-id 831;
    }
    VLAN833 {
        vlan-id 833;
    }
    VLAN835 {
        vlan-id 835;
    }
    VLAN836 {
        vlan-id 836;
    }
    VLAN837 {
        vlan-id 837;
    }
    VLAN839 {
        vlan-id 839;
    }                                   
    VLAN840 {
        vlan-id 840;
    }
    VLAN841 {
        vlan-id 841;
    }
    VLAN842 {
        vlan-id 842;
    }
    VLAN843 {
        vlan-id 843;
    }
    VLAN844 {
        vlan-id 844;
    }
    VLAN845 {
        vlan-id 845;
    }
    VLAN846 {
        vlan-id 846;
    }
    VLAN847 {
        vlan-id 847;                    
    }
    VLAN848 {
        vlan-id 848;
    }
    VLAN849 {
        vlan-id 849;
    }
    VLAN850 {
        vlan-id 850;
    }
    VLAN851 {
        vlan-id 851;
    }
    VLAN852 {
        vlan-id 852;
    }
    VLAN854 {
        vlan-id 854;
    }
    VLAN855 {
        vlan-id 855;
    }
    VLAN856 {                           
        vlan-id 856;
    }
    VLAN857 {
        vlan-id 857;
    }
    VLAN858 {
        vlan-id 858;
    }
    VLAN859 {
        vlan-id 859;
    }
    VLAN860 {
        vlan-id 860;
    }
    VLAN861 {
        vlan-id 861;
    }
    VLAN862 {
        vlan-id 862;
    }
    VLAN863 {
        vlan-id 863;
    }                                   
    VLAN865 {
        vlan-id 865;
    }
    VLAN866 {
        vlan-id 866;
    }
    VLAN867 {
        vlan-id 867;
    }
    VLAN890 {
        vlan-id 890;
    }
    VLAN891 {
        vlan-id 891;
    }
    VLAN892 {
        vlan-id 892;
    }
    VLAN893 {
        vlan-id 893;
    }
    VLAN894 {
        vlan-id 894;                    
    }
    VLAN895 {
        vlan-id 895;
    }
    VLAN898 {
        vlan-id 898;
    }
    VLAN899 {
        vlan-id 899;
    }
    VLAN900 {
        vlan-id 900;
    }
    VLAN912 {
        vlan-id 912;
    }
    VLAN999 {
        vlan-id 999;
    }
}
"""

converted = """
set version 17.2R3.4
set system login class READ permissions clear
set system login class READ permissions maintenance
set system login class READ permissions network
set system login class READ permissions reset
set system login class READ permissions trace
set system login class READ permissions view
set system login class READ permissions view-configuration
set system login user engineer uid 2999
set system login user engineer class super-user
set system login user engineer authentication encrypted-password /* SECRET-DATA */
set system login user noc-auto uid 4001
set system login user noc-auto class super-user
set system login user noc-auto authentication encrypted-password /* SECRET-DATA */
set system login user noc-write uid 4002
set system login user noc-write class super-user
set system login user noc-write authentication encrypted-password /* SECRET-DATA */
set system login user noc-read uid 4003
set system login user noc-read class READ
set system login user noc-read authentication encrypted-password /* SECRET-DATA */
set system root-authentication encrypted-password /* SECRET-DATA */
set system host-name dar01-dal09
set system domain-name example.com
set system time-zone UTC
set system no-redirects
set system arp aging-timer 5
set system internet-options path-mtu-discovery
set system authentication-order password
set system name-server 12.12.1.222
set system name-server 12.12.1.220
set system services ftp
set system services ssh
set system services netconf ssh port 830
set system syslog archive size 100k
set system syslog user * any emergency
set system syslog host 10.1.1.1 any notice
set system syslog host 10.1.1.2 any notice
set system syslog file messages any any
set system syslog file messages authorization none
set system syslog file messages interactive-commands none
set system syslog file messages match "!(.*not Juniper supported SFP.*|(.*Input IFL not found.*))"
set system syslog file messages explicit-priority
set system syslog file interactive-commands interactive-commands any
set system syslog file interactive-commands explicit-priority
set system syslog file login-attempts authorization any
set system syslog file login-attempts explicit-priority
set system syslog source-address 10.200.1.1
set system ntp server 192.1.1.1
set system ntp server 192.1.1.2
set system ntp server 192.1.1.3
set system ntp server 192.1.1.4
set system ntp server 192.1.1.5
set system ntp server 192.1.1.6
set system ntp server 192.1.1.7
set system ntp server 192.1.1.8
set system ntp server 192.1.1.9
set system ntp server 192.1.1.10
set system ntp server 192.1.1.11
set system ntp server 192.1.1.12
set system ntp source-address 10.200.1.1
set chassis aggregated-devices ethernet device-count 40
set interfaces ge-0/0/0 description "LACP 1 TO SW1"
set interfaces ge-0/0/0 ether-options 802.3ad ae1
set interfaces ge-0/0/1 description "LACP 2 TO SW2"
set interfaces ge-0/0/1 ether-options 802.3ad ae2
set interfaces ge-0/0/2 description "LACP 3 TO SW3"
set interfaces ge-0/0/2 ether-options 802.3ad ae3
set interfaces ge-0/0/3 description "LACP 4 TO SW4"
set interfaces ge-0/0/3 ether-options 802.3ad ae4
set interfaces ge-0/0/4 description "LACP 5 TO SW5"
set interfaces ge-0/0/4 ether-options 802.3ad ae5
set interfaces ge-0/0/5 description "LACP 6 TO SW6"
set interfaces ge-0/0/5 ether-options 802.3ad ae6
set interfaces ge-0/0/6 description "UNUSED"
set interfaces ge-0/0/6 unit 0 family inet
set interfaces ge-0/0/7 description "UNUSED"
set interfaces ge-0/0/7 unit 0 family inet
set interfaces ge-0/0/8 description "UNUSED"
set interfaces ge-0/0/8 unit 0 family inet
set interfaces ge-0/0/9 description "UNUSED"
set interfaces ge-0/0/9 unit 0 family inet
set interfaces ge-0/0/10 description "UNUSED"
set interfaces ge-0/0/10 unit 0 family inet
set interfaces ge-0/0/11 description "UNUSED"
set interfaces ge-0/0/11 unit 0 family inet
set interfaces ge-0/0/12 description "UNUSED"
set interfaces ge-0/0/12 unit 0 family inet
set interfaces ge-0/0/13 description "UNUSED"
set interfaces ge-0/0/13 unit 0 family inet
set interfaces ge-0/0/14 description "UNUSED"
set interfaces ge-0/0/14 unit 0 family inet
set interfaces ge-0/0/15 description "UNUSED"
set interfaces ge-0/0/15 unit 0 family inet
set interfaces ge-0/0/16 description "UNUSED"
set interfaces ge-0/0/16 unit 0 family inet
set interfaces ge-0/0/17 description "UNUSED"
set interfaces ge-0/0/17 unit 0 family inet
set interfaces ge-0/0/18 description "UNUSED"
set interfaces ge-0/0/18 unit 0 family inet
set interfaces ge-0/0/19 description "UNUSED"
set interfaces ge-0/0/19 unit 0 family inet
set interfaces ge-0/0/20 description "UNUSED"
set interfaces ge-0/0/20 unit 0 family inet
set interfaces ge-0/0/21 description "UNUSED"
set interfaces ge-0/0/21 unit 0 family inet
set interfaces ge-0/0/22 description "UNUSED"
set interfaces ge-0/0/22 unit 0 family inet
set interfaces ge-0/0/23 description "UNUSED"
set interfaces ge-0/0/23 unit 0 family inet
set interfaces ge-0/0/24 description "UNUSED"
set interfaces ge-0/0/24 unit 0 family inet
set interfaces ge-0/0/25 description "UNUSED"
set interfaces ge-0/0/25 unit 0 family inet
set interfaces ge-0/0/26 description "UNUSED"
set interfaces ge-0/0/26 unit 0 family inet
set interfaces ge-0/0/27 description "UNUSED"
set interfaces ge-0/0/27 unit 0 family inet
set interfaces ge-0/0/28 description "LACP 101 TO TOR1"
set interfaces ge-0/0/28 ether-options 802.3ad ae101
set interfaces ge-0/0/29 description "LACP 102 TO TOR2"
set interfaces ge-0/0/29 ether-options 802.3ad ae102
set interfaces ge-0/0/30 description "LACP 201 TO FW"
set interfaces ge-0/0/30 ether-options 802.3ad ae201
set interfaces ge-0/0/31 description "LACP 202 TO FW"
set interfaces ge-0/0/31 ether-options 802.3ad ae202
set interfaces xe-0/0/32 description "UNUSED"
set interfaces xe-0/0/32 unit 0 family inet
set interfaces xe-0/0/33 description "UNUSED"
set interfaces xe-0/0/33 unit 0 family inet
set interfaces xe-0/0/34 description "TO BASEMENT"
set interfaces xe-0/0/34 unit 0 family ethernet-switching interface-mode trunk
set interfaces xe-0/0/34 unit 0 family ethernet-switching vlan members VLAN310
set interfaces xe-0/0/34 unit 0 family ethernet-switching vlan members VLAN703
set interfaces xe-0/0/34 unit 0 family ethernet-switching vlan members VLAN704
set interfaces xe-0/0/35 description "LACP 111 linking to TO BR SW1"
set interfaces xe-0/0/35 ether-options 802.3ad ae111
set interfaces ae1 description "Interfaces [ge-0/0/0] TO ISW1"
set interfaces ae1 aggregated-ether-options lacp active
set interfaces ae1 aggregated-ether-options lacp periodic slow
set interfaces ae1 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae1 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae2 description "Interfaces [ge-0/0/1] TO ISW2"
set interfaces ae2 aggregated-ether-options lacp active
set interfaces ae2 aggregated-ether-options lacp periodic slow
set interfaces ae2 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae2 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae3 description "Interfaces [ge-0/0/2] TO ISW3"
set interfaces ae3 aggregated-ether-options lacp active
set interfaces ae3 aggregated-ether-options lacp periodic slow
set interfaces ae3 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae3 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae4 description "Interfaces [ge-0/0/3] TO ISW4"
set interfaces ae4 aggregated-ether-options lacp active
set interfaces ae4 aggregated-ether-options lacp periodic slow
set interfaces ae4 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae4 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae5 description "Interfaces [ge-0/0/4] TO ISW5"
set interfaces ae5 aggregated-ether-options lacp active
set interfaces ae5 aggregated-ether-options lacp periodic slow
set interfaces ae5 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae5 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae6 description "Interfaces [ge-0/0/5] TO ISW6"
set interfaces ae6 aggregated-ether-options lacp active
set interfaces ae6 aggregated-ether-options lacp periodic slow
set interfaces ae6 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae6 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae101 description "Interfaces [ge-0/0/28] TO ACC SW1"
set interfaces ae101 aggregated-ether-options lacp active
set interfaces ae101 aggregated-ether-options lacp periodic slow
set interfaces ae101 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae101 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae102 description "Interfaces [ge-0/0/29] TO ACC SW2"
set interfaces ae102 aggregated-ether-options lacp active
set interfaces ae102 aggregated-ether-options lacp periodic slow
set interfaces ae102 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN101
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN102
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN103
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN110
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN684
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN310
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN699
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN698
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN702
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN703
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN704
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN705
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN706
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN708
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN709
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN710
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN711
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN712
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN713
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN740
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN741
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN800
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN801
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN802
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN811
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN812
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN813
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN814
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN815
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN816
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN817
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN818
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN819
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN820
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN821
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN822
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN823
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN826
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN827
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN828
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN829
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN830
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN831
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN835
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN839
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN840
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN843
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN844
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN848
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN845
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN846
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN850
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN847
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN849
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN851
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN836
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN837
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN899
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN900
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN912
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN999
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN841
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN842
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN833
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN854
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN855
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN856
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN857
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN858
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN859
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN860
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN891
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN892
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN893
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN895
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN852
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN894
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN861
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN862
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN865
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN866
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN867
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN863
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN898
set interfaces ae102 unit 0 family ethernet-switching vlan members VLAN890
set interfaces ae111 description "Interfaces [xe-0/0/35] to TO BR SW1"
set interfaces ae111 aggregated-ether-options lacp active
set interfaces ae111 aggregated-ether-options lacp periodic slow
set interfaces ae111 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae111 unit 0 family ethernet-switching vlan members all
set interfaces ae201 description "Interfaces [ge-0/0/30] to BR FW1"
set interfaces ae201 aggregated-ether-options lacp active
set interfaces ae201 aggregated-ether-options lacp periodic slow
set interfaces ae201 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae201 unit 0 family ethernet-switching vlan members all
set interfaces ae202 description "Interfaces [ge-0/0/31] to BR FW2"
set interfaces ae202 aggregated-ether-options lacp active
set interfaces ae202 aggregated-ether-options lacp periodic slow
set interfaces ae202 unit 0 family ethernet-switching interface-mode trunk
set interfaces ae202 unit 0 family ethernet-switching vlan members all
set interfaces irb description "mgmt"
set interfaces irb unit 698 family inet address 10.200.1.1/22
set interfaces vme description "oob"
set interfaces vme unit 0 family inet address 10.30.0.22/8
set snmp location DAL09
set snmp v3 usm local-engine user POLLER-1 authentication-sha authentication-key /* SECRET-DATA */
set snmp v3 usm local-engine user POLLER-1 privacy-aes128 privacy-key /* SECRET-DATA */
set snmp v3 usm local-engine user POLLER-2 authentication-sha authentication-key /* SECRET-DATA */
set snmp v3 usm local-engine user POLLER-2 privacy-aes128 privacy-key /* SECRET-DATA */
set snmp v3 vacm security-to-group security-model usm security-name POLLER-1 group view-all
set snmp v3 vacm security-to-group security-model usm security-name POLLER-2 group view-all
set snmp v3 vacm access group view-all default-context-prefix security-model usm security-level privacy read-view view-all
set snmp engine-id local dar01-dal09
set snmp view view-all oid .1 include
set forwarding-options storm-control-profiles default all
set routing-options static route 0.0.0.0/0 next-hop 10.0.0.1
set routing-options static route 1.0.0.0/16 next-hop 2.0.0.254
set routing-options static route 1.31.0.0/16 next-hop 2.0.0.254
set protocols lldp port-description-type interface-description
set protocols lldp interface all
set protocols lldp interface me0 disable
set protocols lldp-med interface all
set protocols lldp-med interface me0 disable
set protocols mstp bridge-priority 8k
set protocols mstp bpdu-block-on-edge
set protocols mstp interface xe-0/0/34
set protocols mstp interface ae1
set protocols mstp interface ae2
set protocols mstp interface ae3
set protocols mstp interface ae4
set protocols mstp interface ae5
set protocols mstp interface ae6
set protocols mstp interface ae101
set protocols mstp interface ae102
set protocols mstp interface ae111
set protocols mstp interface ae201
set protocols mstp interface ae202
set poe interface all
set vlans VLAN101 vlan-id 101
set vlans VLAN102 vlan-id 102
set vlans VLAN103 vlan-id 103
set vlans VLAN110 vlan-id 110
set vlans VLAN310 vlan-id 310
set vlans VLAN684 vlan-id 684
set vlans VLAN697 vlan-id 697
set vlans VLAN698 vlan-id 698
set vlans VLAN698 l3-interface irb.698
set vlans VLAN699 vlan-id 699
set vlans VLAN702 vlan-id 702
set vlans VLAN703 vlan-id 703
set vlans VLAN704 vlan-id 704
set vlans VLAN705 vlan-id 705
set vlans VLAN706 vlan-id 706
set vlans VLAN708 vlan-id 708
set vlans VLAN709 vlan-id 709
set vlans VLAN710 vlan-id 710
set vlans VLAN711 vlan-id 711
set vlans VLAN712 vlan-id 712
set vlans VLAN713 vlan-id 713
set vlans VLAN740 vlan-id 740
set vlans VLAN741 vlan-id 741
set vlans VLAN800 vlan-id 800
set vlans VLAN801 vlan-id 801
set vlans VLAN802 vlan-id 802
set vlans VLAN811 vlan-id 811
set vlans VLAN812 vlan-id 812
set vlans VLAN813 vlan-id 813
set vlans VLAN814 vlan-id 814
set vlans VLAN815 vlan-id 815
set vlans VLAN816 vlan-id 816
set vlans VLAN817 vlan-id 817
set vlans VLAN818 vlan-id 818
set vlans VLAN819 vlan-id 819
set vlans VLAN820 vlan-id 820
set vlans VLAN821 vlan-id 821
set vlans VLAN822 vlan-id 822
set vlans VLAN823 vlan-id 823
set vlans VLAN824 vlan-id 824
set vlans VLAN826 vlan-id 826
set vlans VLAN827 vlan-id 827
set vlans VLAN828 vlan-id 828
set vlans VLAN829 vlan-id 829
set vlans VLAN830 vlan-id 830
set vlans VLAN831 vlan-id 831
set vlans VLAN833 vlan-id 833
set vlans VLAN835 vlan-id 835
set vlans VLAN836 vlan-id 836
set vlans VLAN837 vlan-id 837
set vlans VLAN839 vlan-id 839
set vlans VLAN840 vlan-id 840
set vlans VLAN841 vlan-id 841
set vlans VLAN842 vlan-id 842
set vlans VLAN843 vlan-id 843
set vlans VLAN844 vlan-id 844
set vlans VLAN845 vlan-id 845
set vlans VLAN846 vlan-id 846
set vlans VLAN847 vlan-id 847
set vlans VLAN848 vlan-id 848
set vlans VLAN849 vlan-id 849
set vlans VLAN850 vlan-id 850
set vlans VLAN851 vlan-id 851
set vlans VLAN852 vlan-id 852
set vlans VLAN854 vlan-id 854
set vlans VLAN855 vlan-id 855
set vlans VLAN856 vlan-id 856
set vlans VLAN857 vlan-id 857
set vlans VLAN858 vlan-id 858
set vlans VLAN859 vlan-id 859
set vlans VLAN860 vlan-id 860
set vlans VLAN861 vlan-id 861
set vlans VLAN862 vlan-id 862
set vlans VLAN863 vlan-id 863
set vlans VLAN865 vlan-id 865
set vlans VLAN866 vlan-id 866
set vlans VLAN867 vlan-id 867
set vlans VLAN890 vlan-id 890
set vlans VLAN891 vlan-id 891
set vlans VLAN892 vlan-id 892
set vlans VLAN893 vlan-id 893
set vlans VLAN894 vlan-id 894
set vlans VLAN895 vlan-id 895
set vlans VLAN898 vlan-id 898
set vlans VLAN899 vlan-id 899
set vlans VLAN900 vlan-id 900
set vlans VLAN912 vlan-id 912
set vlans VLAN999 vlan-id 999
"""

lexer = Lexer(source=original)
lexer.read_tokens()
pprint.pprint(lexer.tokens)

cb = ConfigWriter(tokens=lexer.tokens)
outcome = cb.build_set_config()
print(outcome)
print(converted)
# breakpoint()
print(bool(outcome.strip() == converted.strip()))
