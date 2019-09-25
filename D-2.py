class SemanticVersion:
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, other):
        if not isinstance(other, SemanticVersion):
            return NotImplemented
        if self.major != other.major:
            return False
        if self.minor != other.minor:
            return False
        if self.patch != other.patch:
            return False
        return True

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


def main():
    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    print('3.7.0' == str(py370))  # True


if __name__ == '__main__':
    main()
