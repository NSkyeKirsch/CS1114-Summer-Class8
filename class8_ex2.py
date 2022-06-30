class Weight:
    # store value of weight in both ounces and pounds
    def __init__(self, lbs, ozs):
        self.pounds = lbs
        self.ounces = ozs

    def __str__(self):
        return str(self.pounds) + 'lbs' + str(self.ounces) + 'oz.'

    def __neg__(self):
        return Weight(-self.pounds, self.ounces)

    def __mul__(self, other):
        # MULT of 2 weights is converted each to oz, multiply, convert back to lbs and oz
        self_ounces = self.get_num_ounces()
        other_ounces = other.get_num_ounces()

        new_weight = self_ounces * other_ounces
        return Weight(new_weight // 16, new_weight % 16)

    def get_num_ounces(self):
        return self.pounds * 16 + self.ounces


package_1_weight = Weight(10, 13)
package_2_weight = Weight(5, 12)
package_3_weight = Weight(-1, 0)

print(package_1_weight)
print(-package_2_weight)

new_package_weight = -package_3_weight  # package_3_weight.__neg__()
print(new_package_weight)

big_package = package_1_weight * package_2_weight  # package_1_weight.__mul__(package_2_weight)
print(big_package)
