from ping import pingtest


#usage:
#go to parentdirectory,list out the contents, ping
#                                               |-ping.py
#                                               |-test_ping.py
#command:pytest ping -vs
#            or
#        pytest ping -vsk <key_word:Eg:with_a>


def test_pingtest():
    assert pingtest('','8.8.8.8') == True

def test_NGpingtest():
    assert pingtest('','8.8.8.7') == False

def test_with_n_option():
    assert pingtest('-n','8.8.8.8') == True

def test_NGwith_n_option():
    assert pingtest('-n','8.8.8.7') == False

def test_with_a_option():
    assert pingtest('-a','8.8.8.8') == True

def test_NGwith_a_option():
    assert pingtest('-a','8.8.8.7') == False

def test_with_l_option():
    assert pingtest('-l','8.8.8.8') == True

def test_NGwith_l_option():
    assert pingtest('-l','8.8.8.7') == False