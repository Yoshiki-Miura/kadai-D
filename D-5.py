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
        new_patch = self.patch + 1
        return SemanticVersion(self.major, self.minor, new_patch)

    def minor_version_up(self):
        new_minor = self.minor + 1
        new_patch = 0
        return SemanticVersion(self.major, new_minor, new_patch)

    def major_version_up(self):
        new_major = self.major + 1
        new_minor = 0
        new_patch = 0
        return SemanticVersion(new_major, new_minor, new_patch)


def main():
    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    py400 = py370.major_version_up()
    print(SemanticVersion(4, 0, 0) == py400)  # True


if __name__ == '__main__':
    main()
