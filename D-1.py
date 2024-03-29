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

    def patch_version_up(self):
        self.patch += 1
        return SemanticVersion(self.major, self.minor, self.patch)

    def _version_up(self):
        self.patch += 1
        return SemanticVersion(self.major, self.minor, self.patch)


def main():
    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    # 等価である場合
    print(SemanticVersion(3, 7, 0) == py370)  # True

    # 等価でない場合
    print(SemanticVersion(3, 7, 1) == py370)  # False

    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    print('3.7.0' == str(py370))  # True

    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)  # True


if __name__ == '__main__':
    main()
