import dataclasses
import enum


class Platform(enum.StrEnum):
    QEMU = "qemu"
    METAL = "metal"


class Format(enum.StrEnum):
    QCOW2 = "qcow2"
    ISO = "iso"
    RAW = "raw"


@dataclasses.dataclass
class Artifact:
    location: str
    signature: str
    uncompressed: str
    uncompressed_signature: str


@dataclasses.dataclass
class Build:
    platform: Platform
    fmt: Format
    disk: Artifact | None = None
    kernel: Artifact | None = None
    initrd: Artifact | None = None
    rootfs: Artifact | None = None


ALLOWED_FORMATS = {
    Platform.QEMU: {
        Format.QCOW2,
    },
    Platform.METAL: {
        Format.ISO,
        Format.RAW,
    }
}


