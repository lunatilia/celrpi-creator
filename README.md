# celrpi-creator

Creating CentOS Stream Userland 9 OS Image for Raspberry Pi 4 and 5.

## Examples

### Execution Environment

- CentOS Stream 9 (x86_64)
- Environment constructed with standard partition configuration
- podman installed

#### Change SELinux to Permissive

```
setenforce 0
```

#### Execute qemu-user-static

```
podman run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

#### Build celrpi-creator

```
podman build -t celrpi-creator:el9 docker/
```

#### Build the CentOS Stream Userland 9 OS Image

```
mkdir release
podman run --privileged --rm -it \
-v /lib/modules:/lib/modules:ro \
-v /dev:/dev \
-v $PWD/release:/release \
-v $PWD/kickstart:/BUILDDIR/kickstart \
-t celrpi-creator:el9 \
celrpi-creator --config kickstart/csu9rpi-minimal-ks.cfg --name CentOS-Stream-Userland-9-rpi-minimal
```

