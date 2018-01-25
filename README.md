# Ansible UFW Cluster

[![Build Status](https://travis-ci.org/thomasjpfan/ansible-ufw-cluster-role.svg?branch=master)](https://travis-ci.org/thomasjpfan/ansible-ufw-cluster-role)

Configures UFW to allow port access between a cluster of hosts.

## Role Variables

```yaml
# Apt update time for installing ufw
ufw_apt_valid_item: 86400

# Network interface to allow ports through in cluster
ufw_network_interface: "{{ ansible_default_ipv4['interface'] }}"

# ufw logging
ufw_logging: "off"

# Configurations between hosts in cluster
ufw_cluster_rules: [{ port: 8080, rule: allow }]
# Configurations in general
ufw_general_ports: [{ port: 22, rule: allow}]
```

## Testing

This project uses [ansible-ubuntu-local-runner)](https://github.com/thomasjpfan/ansible-ubuntu-local-runner) to run tests in a docker container.

1. Start Container for testing:

```bash
make setup_test
```

2. Run Tests

```bash
make test
```

3. Stop up container

```bash
make clean_up
```

## Local Testing

The `tests/playbook.yml` file includes a pre-tasks that adds a ubuntu cacher configuration for local testing. You can start your own cacher by running:

```bash
docker network create ng
docker run --name apt-cacher -d --restart=always \
  --publish 3142:3142 \
  --volume /srv/docker/apt-cacher-ng:/var/cache/apt-cacher-ng \
  --network ng \
  sameersbn/apt-cacher-ng:latest
```

To use to cache for local testing run `make setup_test_local` instead of `make setup_test`.

## License

MIT