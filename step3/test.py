test_links = []
with open("links_for_test") as f:
    test_links = f.readlines()
test_links = [line.rstrip() for line in test_links]
print(test_links)