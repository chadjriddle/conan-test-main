from conans import ConanFile
from conans import CMake


class ConanTestMain(ConanFile):
    """Build Conan Test Main"""
    name = "conan-test-main"
    version = "0.1.0"
    url = "https://github.com/chadjriddle/conan-test-main"
    author = "chadjriddle"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports = "*"
    description = "Conan Test Application Main Project"
    requires = "gtest/cci.20210126"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def build(self):
        shared = {"BUILD_SHARED_LIBS": self.options.shared}
        cmake = CMake(self)
        cmake.configure(defs=shared)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", src="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.exe", src="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["conan-test-main"]