.PHONY: clean

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-test - remove test and coverage artifacts"

clean: clean-dist clean-test

clean-dist:
	rm -f *.tar.gz

clean-test:
	rm -fr tests/output
