from conans import ConanFile, tools


class PrintConan(ConanFile):
    name = "print"
    version = "0.0.0"
    license = "MIT"
    url = "https://github.com/danimtb/conan-print"
    description = "Print execution of methods of a conanfile.py for each Conan command"
    exports = "LICENSE"

    def source(self):
        self.output.info("source()")

    def build(self):
        self.output.info("build()")

    def package(self):
        self.output.info("package()")

    def package_info(self):
        self.output.info("package_info()")

    def configure(self):
        self.output.info("configure()")

    def config_options(self):
        self.output.info("config_options()")

    def requirements(self):
        self.output.info("requirements()")

    def build_requirements(self):
        self.output.info("build_requirements()")

    def system_requirements(self):
        self.output.info("system_requirements()")

    def imports(self):
        self.output.info("imports()")

    def package_id(self):
        self.output.info("package_id()")

    def buiild_id(self):
        self.output.info("build_id()")

    def deploy(self):
        self.output.info("deploy()")
