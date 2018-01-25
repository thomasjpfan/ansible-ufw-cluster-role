import re


def test_ufw_started(host):
    service = host.service('ufw')

    assert service.is_enabled
    assert service.is_running


def test_ufw_ports(host):
    ufw_status = host.run("ufw status")
    assert not ufw_status.rc

    output = ufw_status.stdout
    match_22 = re.findall("22\s+ALLOW\s+Anywhere", output, re.MULTILINE)
    assert match_22

    match_8080 = re.findall("8080\s+ALLOW[\s\.]+", output)
    assert len(match_8080) == 2
