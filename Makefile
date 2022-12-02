all:
	python3 setup.py build_ext --inplace

.PHONY: clean
clean:
	$(RM) -rf *.c *.so build .mypy_cache
