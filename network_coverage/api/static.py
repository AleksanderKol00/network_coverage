from attr import dataclass


@dataclass
class NetworkCoverage:
    n_2G: bool
    n_3G: bool
    n_4G: bool
