"""
  ==========================================
  || FreeCodeCamp – Daily Coding Challenge ||
  || Date: 2026-08-09                      ||
  || Dominik Łempicki (kapitan)            ||
  ==========================================
"""

def mix_paint(bucket1, bucket2):

    return [round((kolor1 * bucket1["fullness"] + kolor2 * bucket2["fullness"]) / (bucket1["fullness"] + bucket2["fullness"]))   for kolor1,kolor2 in zip(bucket1["color"],bucket2["color"])]

print(mix_paint({"color": [250, 250, 250], "fullness": 50}, {"color": [0, 0, 0], "fullness": 50}))
print(mix_paint({"color": [143, 143, 101], "fullness": 45}, {"color": [100, 204, 204], "fullness": 90}))