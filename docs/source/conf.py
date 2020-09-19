project = "Test Ansible Collection"
copyright = "2020, Michael Richardson"
author = "Michael Richardson"

extensions = [
    "sphinx_rtd_theme",
]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_context = {
    "display_github": True,
    "github_user": "mrichardson03",
    "github_repo": "ansible-test-collection",
    "github_version": "master",
    "conf_py_path": "/docs/source/",
}