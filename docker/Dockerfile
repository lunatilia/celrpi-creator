FROM quay.io/centos/arm64v8:stream9

ENV TZ=Asia/Tokyo

COPY [ "patch/", "/tmp/" ]
COPY [ "celrpi-creator", "/usr/local/bin/" ]

RUN /usr/bin/dnf --nodocs -y update \
 && /usr/bin/dnf --nodocs -y install python39 lorax-lmc-novirt patch subscription-manager \
 && /usr/bin/dnf --nodocs -y reinstall tzdata \
 && /usr/bin/dnf clean all \
 && mkdir -p /{release,BUILDDIR/tmp,BUILDDIR/kickstart,BUILDDIR/log} \
 && patch -u -b /usr/lib64/python3.9/site-packages/pyanaconda/modules/storage/platform.py < /tmp/platform.py.patch \
 && patch -u -b /usr/lib64/python3.9/site-packages/pyanaconda/modules/storage/initialization.py < /tmp/initialization.py.patch \
 && patch -u -b /usr/lib64/python3.9/site-packages/pyanaconda/modules/storage/bootloader/factory.py < /tmp/factory.py.patch \
 && cp -a /tmp/rpi.py  /usr/lib64/python3.9/site-packages/pyanaconda/modules/storage/bootloader/ \
 && curl -L -o /usr/local/bin/entrypoint.sh \
 https://raw.githubusercontent.com/AkihiroSuda/containerized-systemd/master/docker-entrypoint.sh \
 && chmod +x /usr/local/bin/entrypoint.sh \
 && patch -u -b /usr/local/bin/entrypoint.sh < /tmp/entrypoint.sh.patch \
 && rm -rf /tmp/*

WORKDIR /BUILDDIR

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
