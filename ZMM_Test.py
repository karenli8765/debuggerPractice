import unittest
from ZorkMazeManager import ZorkMazeManager


class MyZZMTestCase(unittest.TestCase):

    def test_a_simple_string_match(self):
        zmm = ZorkMazeManager(hop_interval=5, clap_interval=7, pat_interval=11, num_vals=10)
        output = zmm.__str__()
        expected = "5\thop \n7\tclap\n"
        self.assertEqual(expected, output, "basic string did not match")

    @unittest.skip("Skipping test b. Get test a working first.")
    def test_b_hop_and_clap(self):
        zmm = ZorkMazeManager(hop_interval=5, clap_interval=7, pat_interval=11, num_vals=40)
        output = zmm.__str__()
        expected = "5\thop \n7\tclap\n10\thop \n11\tpat \n14\tclap\n15\thop \n20\thop \n21\tclap\n22\tpat \n25\thop " \
                   "\n28\tclap\n30\thop \n33\tpat \n35\thop \tclap\n"
        self.assertEqual(expected, output, "hop_and_clap string did not match.")

    @unittest.skip("Skipping test c. Get test b working first.")
    def test_c_hop_and_pat(self):
        zmm = ZorkMazeManager(hop_interval=5, clap_interval=7, pat_interval=11, num_vals=60)
        output = zmm.__str__()
        expected = "5\thop \n7\tclap\n10\thop \n11\tpat \n14\tclap\n15\thop \n20\thop \n21\tclap\n22\tpat \n25\thop " \
                   "\n28\tclap\n30\thop \n33\tpat \n35\thop \tclap\n40\thop \n42\tclap\n44\tpat \n45\thop " \
                   "\n49\tclap\n50\thop \n55\thop \tpat \n56\tclap\n"
        self.assertEqual(expected, output, "hop_and_pat string did not match.")

    @unittest.skip("Skipping test d. Get test c working first.")
    def test_d_clap_and_pat(self):
        zmm = ZorkMazeManager(hop_interval=5, clap_interval=7, pat_interval=11, num_vals=80)
        output = zmm.__str__()
        expected = "5\thop \n7\tclap\n10\thop \n11\tpat \n14\tclap\n15\thop \n20\thop \n21\tclap\n22\tpat \n25\thop " \
                   "\n28\tclap\n30\thop \n33\tpat \n35\thop \tclap\n40\thop \n42\tclap\n44\tpat \n45\thop " \
                   "\n49\tclap\n50\thop \n55\thop \tpat \n56\tclap\n60\thop \n63\tclap\n65\thop \n66\tpat \n70\thop " \
                   "\tclap\n75\thop \n77\tclap\tpat \n"
        self.assertEqual(expected, output, "clap_and_pat string did not match.")

    @unittest.skip("Skipping test e. Get test d working first.")
    def test_e_short_hop_clap_pat(self):
        zmm = ZorkMazeManager(hop_interval=3, clap_interval=4, pat_interval=5, num_vals=80)
        output = zmm.__str__()
        expected = "3\thop \n4\tclap\n5\tpat \n6\thop \n8\tclap\n9\thop \n10\tpat \n12\thop \tclap\n15\thop \tpat " \
                   "\n16\tclap\n18\thop \n20\tclap\tpat \n21\thop \n24\thop \tclap\n25\tpat \n27\thop " \
                   "\n28\tclap\n30\thop \tpat \n32\tclap\n33\thop \n35\tpat \n36\thop \tclap\n39\thop " \
                   "\n40\tclap\tpat \n42\thop \n44\tclap\n45\thop \tpat \n48\thop \tclap\n50\tpat \n51\thop " \
                   "\n52\tclap\n54\thop \n55\tpat \n56\tclap\n57\thop \n60\thop \tclap\tpat \n63\thop " \
                   "\n64\tclap\n65\tpat \n66\thop \n68\tclap\n69\thop \n70\tpat \n72\thop \tclap\n75\thop \tpat " \
                   "\n76\tclap\n78\thop \n"
        self.assertEqual(expected, output, "short version of hop/clap/pat didn't work.")

    @unittest.skip("Skipping test f. Get test e working first.")
    def test_f_long_hop_clap_pat(self):
        zmm = ZorkMazeManager(hop_interval=3, pat_interval=5, clap_interval=7, num_vals=200)
        output = zmm.__str__()
        expected = "3\thop \n5\tclap\n6\thop \n7\tpat \n9\thop \n10\tclap\n12\thop \n14\tpat \n15\thop " \
                   "\tclap\n18\thop \n20\tclap\n21\thop \tpat \n24\thop \n25\tclap\n27\thop \n28\tpat \n30\thop " \
                   "\tclap\n33\thop \n35\tclap\tpat \n36\thop \n39\thop \n40\tclap\n42\thop \tpat \n45\thop " \
                   "\tclap\n48\thop \n49\tpat \n50\tclap\n51\thop \n54\thop \n55\tclap\n56\tpat \n57\thop \n60\thop " \
                   "\tclap\n63\thop \tpat \n65\tclap\n66\thop \n69\thop \n70\tclap\tpat \n72\thop \n75\thop " \
                   "\tclap\n77\tpat \n78\thop \n80\tclap\n81\thop \n84\thop \tpat \n85\tclap\n87\thop \n90\thop " \
                   "\tclap\n91\tpat \n93\thop \n95\tclap\n96\thop \n98\tpat \n99\thop \n100\tclap\n102\thop " \
                   "\n105\thop \tclap\tpat \n108\thop \n110\tclap\n111\thop \n112\tpat \n114\thop " \
                   "\n115\tclap\n117\thop \n119\tpat \n120\thop \tclap\n123\thop \n125\tclap\n126\thop \tpat " \
                   "\n129\thop \n130\tclap\n132\thop \n133\tpat \n135\thop \tclap\n138\thop \n140\tclap\tpat " \
                   "\n141\thop \n144\thop \n145\tclap\n147\thop \tpat \n150\thop \tclap\n153\thop \n154\tpat " \
                   "\n155\tclap\n156\thop \n159\thop \n160\tclap\n161\tpat \n162\thop \n165\thop \tclap\n168\thop " \
                   "\tpat \n170\tclap\n171\thop \n174\thop \n175\tclap\tpat \n177\thop \n180\thop \tclap\n182\tpat " \
                   "\n183\thop \n185\tclap\n186\thop \n189\thop \tpat \n190\tclap\n192\thop \n195\thop " \
                   "\tclap\n196\tpat \n198\thop \n"
        self.assertEqual(expected, output, "long version of hop/clap/pat didn't work.")


if __name__ == '__main__':
    unittest.main()
