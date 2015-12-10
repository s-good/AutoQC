import numpy as np
import qctests.CoTeDe_anomaly_detection
import util.testingProfile

'''Tests to ensure that we are running the CoTeDe tests
   as expected. The data are from the seabird package
   tests (file dPIRX010.cnv) and QC decisions are produced
   by running that file natively through the CoTeDe package.
'''

def test_CoTeDe_anomaly_detection():
    '''
    Make sure CoTeDe anomaly detection is working as expected.
    '''
    qc = qctests.CoTeDe_anomaly_detection.test(p)
    assert np.array_equal(qc, expected_qc_anomaly_detection), 'mismatch between qc results and expected values'


# Data and QC decisions - extracted from the seabird tests,
# file dPIRX010.cnv.
# Seabird (https://github.com/castelao/seabird) is copyright (c) 2011-2015, Guilherme Pimenta Castelao.
data = np.array([
[ 1.0 , 27.4365 , 35.3159 ],
[ 2.0 , 27.4461 , 35.8232 ],
[ 3.0 , 27.4506 , 35.7264 ],
[ 4.0 , 27.4499 , 35.7262 ],
[ 5.0 , 27.4492 , 35.7249 ],
[ 6.0 , 27.4482 , 35.724 ],
[ 7.0 , 27.4475 , 35.7234 ],
[ 8.0 , 27.4465 , 35.7233 ],
[ 9.0 , 27.4474 , 35.7234 ],
[ 10.0 , 27.4481 , 35.7233 ],
[ 11.0 , 27.4474 , 35.7236 ],
[ 12.0 , 27.4477 , 35.7235 ],
[ 13.0 , 27.4482 , 35.7236 ],
[ 14.0 , 27.4491 , 35.7231 ],
[ 15.0 , 27.4506 , 35.7349 ],
[ 16.0 , 27.4511 , 35.7447 ],
[ 17.0 , 27.4518 , 35.7434 ],
[ 18.0 , 27.4509 , 35.7504 ],
[ 19.0 , 27.4517 , 35.75 ],
[ 20.0 , 27.4522 , 35.7491 ],
[ 21.0 , 27.4528 , 35.7467 ],
[ 22.0 , 27.4516 , 35.75 ],
[ 23.0 , 27.4485 , 35.7553 ],
[ 24.0 , 27.4449 , 35.7613 ],
[ 25.0 , 27.4437 , 35.7625 ],
[ 26.0 , 27.4429 , 35.7628 ],
[ 27.0 , 27.4364 , 35.7686 ],
[ 28.0 , 27.4339 , 35.771 ],
[ 29.0 , 27.4253 , 35.7785 ],
[ 30.0 , 27.4114 , 35.7912 ],
[ 31.0 , 27.4043 , 35.7968 ],
[ 32.0 , 27.404 , 35.7987 ],
[ 33.0 , 27.401 , 35.7988 ],
[ 34.0 , 27.3981 , 35.7985 ],
[ 35.0 , 27.396 , 35.7986 ],
[ 36.0 , 27.3952 , 35.7986 ],
[ 37.0 , 27.3937 , 35.8003 ],
[ 38.0 , 27.3764 , 35.8064 ],
[ 39.0 , 27.2958 , 35.8472 ],
[ 40.0 , 27.1237 , 35.9385 ],
[ 41.0 , 26.9626 , 36.0256 ],
[ 42.0 , 26.6479 , 36.1505 ],
[ 43.0 , 26.375 , 36.2186 ],
[ 44.0 , 25.9358 , 36.3068 ],
[ 45.0 , 25.821 , 36.3194 ],
[ 46.0 , 25.8024 , 36.3207 ],
[ 47.0 , 25.79 , 36.3227 ],
[ 48.0 , 25.7494 , 36.3261 ],
[ 49.0 , 25.641 , 36.3301 ],
[ 50.0 , 25.4406 , 36.3315 ],
[ 51.0 , 25.2774 , 36.3284 ],
[ 52.0 , 24.9462 , 36.3322 ],
[ 53.0 , 24.7947 , 36.3354 ],
[ 54.0 , 24.7345 , 36.3432 ],
[ 55.0 , 24.6941 , 36.3513 ],
[ 56.0 , 24.6248 , 36.3605 ],
[ 57.0 , 24.5066 , 36.3814 ],
[ 58.0 , 24.4924 , 36.3849 ],
[ 59.0 , 24.4617 , 36.3914 ],
[ 60.0 , 24.3244 , 36.3986 ],
[ 61.0 , 24.0119 , 36.4199 ],
[ 62.0 , 23.5658 , 36.4092 ],
[ 63.0 , 23.1143 , 36.3864 ],
[ 64.0 , 22.9155 , 36.3672 ],
[ 65.0 , 22.8114 , 36.3713 ],
[ 66.0 , 22.5472 , 36.3577 ],
[ 67.0 , 22.3186 , 36.3455 ],
[ 68.0 , 21.8833 , 36.3176 ],
[ 69.0 , 20.8729 , 36.2531 ],
[ 70.0 , 19.842 , 36.1708 ],
[ 71.0 , 19.5595 , 36.1399 ],
[ 72.0 , 19.4807 , 36.1301 ],
[ 73.0 , 19.4079 , 36.1244 ],
[ 74.0 , 19.3391 , 36.1221 ],
[ 75.0 , 19.1495 , 36.1078 ],
[ 76.0 , 18.9326 , 36.0876 ],
[ 77.0 , 18.8371 , 36.0738 ],
[ 78.0 , 18.6738 , 36.0563 ],
[ 79.0 , 18.4649 , 36.0345 ],
[ 80.0 , 18.3533 , 36.0214 ],
[ 81.0 , 18.2121 , 36.007 ],
[ 82.0 , 18.1679 , 36.0048 ],
[ 83.0 , 18.1017 , 35.9987 ],
[ 84.0 , 17.984 , 35.9852 ],
[ 85.0 , 17.7601 , 35.9567 ],
[ 86.0 , 17.501 , 35.9334 ],
[ 87.0 , 17.3033 , 35.9038 ],
[ 88.0 , 17.1672 , 35.881 ],
[ 89.0 , 17.0637 , 35.8618 ],
[ 90.0 , 16.8609 , 35.8459 ],
[ 91.0 , 16.6222 , 35.8126 ],
[ 92.0 , 16.2709 , 35.7626 ],
[ 93.0 , 15.9205 , 35.7155 ],
[ 94.0 , 15.5989 , 35.6739 ],
[ 95.0 , 15.2665 , 35.6268 ],
[ 96.0 , 15.0293 , 35.6105 ],
[ 97.0 , 14.8829 , 35.5752 ],
[ 98.0 , 14.803 , 35.567 ],
[ 99.0 , 14.6668 , 35.5434 ],
[ 100.0 , 14.5719 , 35.5276 ],
[ 101.0 , 14.3824 , 35.5039 ],
[ 102.0 , 14.3197 , 35.491 ],
[ 103.0 , 14.2946 , 35.4867 ],
[ 104.0 , 14.2477 , 35.4811 ],
[ 105.0 , 14.2512 , 35.4828 ],
[ 106.0 , 14.2473 , 35.4825 ],
[ 107.0 , 14.2406 , 35.4815 ],
[ 108.0 , 14.224 , 35.4789 ],
[ 109.0 , 14.1992 , 35.4743 ],
[ 110.0 , 14.182 , 35.4709 ],
[ 111.0 , 14.1511 , 35.4662 ],
[ 112.0 , 14.1233 , 35.4616 ],
[ 113.0 , 14.0342 , 35.4442 ],
[ 114.0 , 13.9714 , 35.4343 ],
[ 115.0 , 13.9395 , 35.4299 ],
[ 116.0 , 13.9314 , 35.4288 ],
[ 117.0 , 13.9263 , 35.4283 ],
[ 118.0 , 13.9108 , 35.4253 ],
[ 119.0 , 13.8916 , 35.422 ],
[ 120.0 , 13.8329 , 35.4121 ],
[ 121.0 , 13.7149 , 35.3915 ],
[ 122.0 , 13.5243 , 35.365 ],
[ 123.0 , 13.355 , 35.3366 ],
[ 124.0 , 13.3051 , 35.3298 ],
[ 125.0 , 13.2753 , 35.3237 ],
[ 126.0 , 13.2595 , 35.3203 ],
[ 127.0 , 13.2079 , 35.3137 ],
[ 128.0 , 13.15 , 35.3061 ],
[ 129.0 , 13.1445 , 35.3056 ],
[ 130.0 , 13.1332 , 35.3039 ],
[ 131.0 , 13.1245 , 35.3027 ],
[ 132.0 , 13.1199 , 35.3021 ],
[ 133.0 , 13.1139 , 35.3013 ],
[ 134.0 , 13.1043 , 35.3001 ],
[ 135.0 , 13.0971 , 35.2994 ],
[ 136.0 , 13.0878 , 35.2987 ],
[ 137.0 , 13.0794 , 35.2978 ],
[ 138.0 , 13.0628 , 35.2947 ],
[ 139.0 , 13.0489 , 35.2926 ],
[ 140.0 , 13.0344 , 35.2905 ],
[ 141.0 , 13.0211 , 35.2895 ],
[ 142.0 , 12.9665 , 35.2836 ],
[ 143.0 , 12.9 , 35.2731 ],
[ 144.0 , 12.8632 , 35.2661 ],
[ 145.0 , 12.8344 , 35.2619 ],
[ 146.0 , 12.8044 , 35.2581 ],
[ 147.0 , 12.7782 , 35.2549 ],
[ 148.0 , 12.7601 , 35.2516 ],
[ 149.0 , 12.7321 , 35.2481 ],
[ 150.0 , 12.699 , 35.2442 ],
[ 151.0 , 12.6833 , 35.2412 ],
[ 152.0 , 12.6693 , 35.2382 ],
[ 153.0 , 12.6537 , 35.2368 ],
[ 154.0 , 12.6185 , 35.2324 ],
[ 155.0 , 12.5931 , 35.2281 ],
[ 156.0 , 12.5653 , 35.2241 ],
[ 157.0 , 12.5546 , 35.2227 ],
[ 158.0 , 12.5448 , 35.2211 ],
[ 159.0 , 12.5319 , 35.2196 ],
[ 160.0 , 12.5136 , 35.2168 ],
[ 161.0 , 12.4903 , 35.2132 ],
[ 162.0 , 12.4766 , 35.2117 ],
[ 163.0 , 12.4651 , 35.2094 ],
[ 164.0 , 12.4539 , 35.2077 ],
[ 165.0 , 12.4442 , 35.2064 ],
[ 166.0 , 12.4271 , 35.2045 ],
[ 167.0 , 12.3964 , 35.1999 ],
[ 168.0 , 12.3749 , 35.1962 ],
[ 169.0 , 12.362 , 35.1945 ],
[ 170.0 , 12.3449 , 35.192 ],
[ 171.0 , 12.3286 , 35.1899 ],
[ 172.0 , 12.3184 , 35.1886 ],
[ 173.0 , 12.3117 , 35.1877 ],
[ 174.0 , 12.3078 , 35.1873 ],
[ 175.0 , 12.3044 , 35.1866 ],
[ 176.0 , 12.2997 , 35.1862 ],
[ 177.0 , 12.2898 , 35.1849 ],
[ 178.0 , 12.277 , 35.1828 ],
[ 179.0 , 12.2696 , 35.1815 ],
[ 180.0 , 12.2697 , 35.1818 ],
[ 181.0 , 12.2676 , 35.1813 ],
[ 182.0 , 12.2596 , 35.1802 ],
[ 183.0 , 12.2508 , 35.179 ],
[ 184.0 , 12.2375 , 35.1771 ],
[ 185.0 , 12.2136 , 35.1742 ],
[ 186.0 , 12.1942 , 35.1717 ],
[ 187.0 , 12.1756 , 35.1696 ],
[ 188.0 , 12.1662 , 35.1685 ],
[ 189.0 , 12.1632 , 35.1684 ],
[ 190.0 , 12.1594 , 35.1682 ],
[ 191.0 , 12.1526 , 35.1675 ],
[ 192.0 , 12.1339 , 35.1656 ],
[ 193.0 , 12.09 , 35.162 ],
[ 194.0 , 12.0531 , 35.158 ],
[ 195.0 , 12.0085 , 35.1509 ],
[ 196.0 , 12.0041 , 35.1503 ],
[ 197.0 , 12.0027 , 35.15 ],
[ 198.0 , 11.9957 , 35.1484 ],
[ 199.0 , 11.9783 , 35.1467 ],
[ 200.0 , 11.954 , 35.1437 ],
[ 201.0 , 11.931 , 35.1413 ],
[ 202.0 , 11.9004 , 35.1378 ],
[ 203.0 , 11.8786 , 35.1348 ],
[ 204.0 , 11.8739 , 35.1342 ],
[ 205.0 , 11.8638 , 35.1326 ],
[ 206.0 , 11.8406 , 35.1296 ],
[ 207.0 , 11.8078 , 35.1257 ],
[ 208.0 , 11.7942 , 35.124 ],
[ 209.0 , 11.7936 , 35.1241 ],
[ 210.0 , 11.7892 , 35.1237 ],
[ 211.0 , 11.7797 , 35.1224 ],
[ 212.0 , 11.7712 , 35.1213 ],
[ 213.0 , 11.7645 , 35.1207 ],
[ 214.0 , 11.7561 , 35.12 ],
[ 215.0 , 11.7539 , 35.1199 ],
[ 216.0 , 11.752 , 35.1195 ],
[ 217.0 , 11.7531 , 35.1199 ],
[ 218.0 , 11.7538 , 35.1202 ],
[ 219.0 , 11.7501 , 35.1199 ],
[ 220.0 , 11.7421 , 35.1191 ],
[ 221.0 , 11.7348 , 35.1182 ],
[ 222.0 , 11.7308 , 35.1174 ],
[ 223.0 , 11.7276 , 35.1167 ],
[ 224.0 , 11.7255 , 35.1163 ],
[ 225.0 , 11.7197 , 35.1157 ],
[ 226.0 , 11.715 , 35.1152 ],
[ 227.0 , 11.7142 , 35.1154 ],
[ 228.0 , 11.7131 , 35.1156 ],
[ 229.0 , 11.7129 , 35.1153 ],
[ 230.0 , 11.7125 , 35.1153 ],
[ 231.0 , 11.7095 , 35.1154 ],
[ 232.0 , 11.6958 , 35.1139 ],
[ 233.0 , 11.6837 , 35.113 ],
[ 234.0 , 11.672 , 35.1125 ],
[ 235.0 , 11.6553 , 35.1106 ],
[ 236.0 , 11.6397 , 35.1094 ],
[ 237.0 , 11.6241 , 35.1071 ],
[ 238.0 , 11.6004 , 35.1045 ],
[ 239.0 , 11.5863 , 35.1026 ],
[ 240.0 , 11.5835 , 35.1023 ],
[ 241.0 , 11.5818 , 35.1021 ],
[ 242.0 , 11.5807 , 35.1018 ],
[ 243.0 , 11.573 , 35.1016 ],
[ 244.0 , 11.5591 , 35.0998 ],
[ 245.0 , 11.5359 , 35.0958 ],
[ 246.0 , 11.5222 , 35.0932 ],
[ 247.0 , 11.5087 , 35.0909 ],
[ 248.0 , 11.4997 , 35.0893 ],
[ 249.0 , 11.4932 , 35.0886 ],
[ 250.0 , 11.49 , 35.0878 ],
[ 251.0 , 11.4887 , 35.0875 ],
[ 252.0 , 11.4858 , 35.0875 ],
[ 253.0 , 11.4825 , 35.087 ],
[ 254.0 , 11.4798 , 35.0867 ],
[ 255.0 , 11.4774 , 35.0865 ],
[ 256.0 , 11.4759 , 35.086 ],
[ 257.0 , 11.4671 , 35.0852 ],
[ 258.0 , 11.4458 , 35.0832 ],
[ 259.0 , 11.4209 , 35.0797 ],
[ 260.0 , 11.3986 , 35.0768 ],
[ 261.0 , 11.3759 , 35.0747 ],
[ 262.0 , 11.3463 , 35.0707 ],
[ 263.0 , 11.3254 , 35.0689 ],
[ 264.0 , 11.3165 , 35.0673 ],
[ 265.0 , 11.3157 , 35.067 ],
[ 266.0 , 11.316 , 35.0679 ],
[ 267.0 , 11.3182 , 35.0696 ],
[ 268.0 , 11.3215 , 35.0708 ],
[ 269.0 , 11.325 , 35.0717 ],
[ 270.0 , 11.3275 , 35.0729 ],
[ 271.0 , 11.328 , 35.0733 ],
[ 272.0 , 11.3227 , 35.0729 ],
[ 273.0 , 11.3069 , 35.0713 ],
[ 274.0 , 11.2935 , 35.0699 ],
[ 275.0 , 11.2892 , 35.0689 ],
[ 276.0 , 11.2841 , 35.0681 ],
[ 277.0 , 11.2738 , 35.0666 ],
[ 278.0 , 11.2682 , 35.0656 ],
[ 279.0 , 11.2612 , 35.0649 ],
[ 280.0 , 11.2516 , 35.0639 ],
[ 281.0 , 11.2436 , 35.0631 ],
[ 282.0 , 11.2394 , 35.0625 ],
[ 283.0 , 11.2281 , 35.0608 ],
[ 284.0 , 11.1997 , 35.0566 ],
[ 285.0 , 11.1622 , 35.0513 ],
[ 286.0 , 11.1538 , 35.0502 ],
[ 287.0 , 11.1427 , 35.0483 ],
[ 288.0 , 11.1362 , 35.0471 ],
[ 289.0 , 11.1316 , 35.0465 ],
[ 290.0 , 11.1219 , 35.0453 ],
[ 291.0 , 11.1186 , 35.0443 ],
[ 292.0 , 11.1167 , 35.044 ],
[ 293.0 , 11.116 , 35.0437 ],
[ 294.0 , 11.115 , 35.044 ],
[ 295.0 , 11.1142 , 35.0438 ],
[ 296.0 , 11.1122 , 35.0431 ],
[ 297.0 , 11.1091 , 35.0424 ],
[ 298.0 , 11.1066 , 35.042 ],
[ 299.0 , 11.0897 , 35.0394 ],
[ 300.0 , 11.0088 , 35.028 ],
[ 301.0 , 10.9601 , 35.0197 ],
[ 302.0 , 10.9335 , 35.0163 ],
[ 303.0 , 10.9226 , 35.0148 ],
[ 304.0 , 10.9218 , 35.0149 ],
[ 305.0 , 10.9212 , 35.0149 ],
[ 306.0 , 10.9115 , 35.0139 ],
[ 307.0 , 10.8854 , 35.0118 ],
[ 308.0 , 10.8668 , 35.01 ],
[ 309.0 , 10.8225 , 35.0061 ],
[ 310.0 , 10.8008 , 35.0056 ],
[ 311.0 , 10.786 , 35.0055 ],
[ 312.0 , 10.78 , 35.0049 ],
[ 313.0 , 10.7734 , 35.0044 ],
[ 314.0 , 10.7598 , 35.0032 ],
[ 315.0 , 10.7393 , 35.0009 ],
[ 316.0 , 10.7428 , 35.0017 ],
[ 317.0 , 10.7416 , 35.0016 ],
[ 318.0 , 10.7389 , 35.0013 ],
[ 319.0 , 10.7323 , 35.0007 ],
[ 320.0 , 10.7244 , 35.0003 ],
[ 321.0 , 10.7109 , 34.9992 ],
[ 322.0 , 10.6856 , 34.9965 ],
[ 323.0 , 10.6667 , 34.9936 ],
[ 324.0 , 10.6478 , 34.9907 ],
[ 325.0 , 10.6219 , 34.9872 ],
[ 326.0 , 10.6056 , 34.9853 ],
[ 327.0 , 10.6005 , 34.9848 ],
[ 328.0 , 10.5939 , 34.9838 ],
[ 329.0 , 10.5914 , 34.9835 ],
[ 330.0 , 10.5861 , 34.9833 ],
[ 331.0 , 10.5798 , 34.983 ],
[ 332.0 , 10.5725 , 34.9827 ],
[ 333.0 , 10.5613 , 34.9822 ],
[ 334.0 , 10.5552 , 34.9818 ],
[ 335.0 , 10.5372 , 34.9813 ],
[ 336.0 , 10.5125 , 34.9789 ],
[ 337.0 , 10.4874 , 34.9762 ],
[ 338.0 , 10.4398 , 34.9723 ],
[ 339.0 , 10.3964 , 34.9689 ],
[ 340.0 , 10.3875 , 34.9701 ],
[ 341.0 , 10.3605 , 34.9715 ],
[ 342.0 , 10.3541 , 34.9726 ],
[ 343.0 , 10.3469 , 34.9743 ],
[ 344.0 , 10.3178 , 34.9718 ],
[ 345.0 , 10.2849 , 34.9684 ],
[ 346.0 , 10.2392 , 34.9634 ],
[ 347.0 , 10.2085 , 34.9592 ],
[ 348.0 , 10.1805 , 34.9557 ],
[ 349.0 , 10.1539 , 34.9536 ],
[ 350.0 , 10.0737 , 34.9459 ],
[ 351.0 , 10.036 , 34.9376 ],
[ 352.0 , 10.0228 , 34.9349 ],
[ 353.0 , 9.9993 , 34.9336 ],
[ 354.0 , 9.9681 , 34.9309 ],
[ 355.0 , 9.9328 , 34.9271 ],
[ 356.0 , 9.8933 , 34.9241 ],
[ 357.0 , 9.8421 , 34.9208 ],
[ 358.0 , 9.7423 , 34.912 ],
[ 359.0 , 9.6051 , 34.8957 ],
[ 360.0 , 9.582 , 34.8934 ],
[ 361.0 , 9.5419 , 34.8915 ],
[ 362.0 , 9.5096 , 34.8873 ],
[ 363.0 , 9.5029 , 34.8858 ],
[ 364.0 , 9.4903 , 34.8843 ],
[ 365.0 , 9.4748 , 34.8834 ],
[ 366.0 , 9.4642 , 34.8828 ],
[ 367.0 , 9.4428 , 34.8807 ],
[ 368.0 , 9.4212 , 34.8776 ],
[ 369.0 , 9.4093 , 34.8751 ],
[ 370.0 , 9.3992 , 34.8745 ],
[ 371.0 , 9.3488 , 34.8694 ],
[ 372.0 , 9.2809 , 34.8622 ],
[ 373.0 , 9.2639 , 34.8599 ],
[ 374.0 , 9.2606 , 34.8599 ],
[ 375.0 , 9.2397 , 34.8579 ],
[ 376.0 , 9.2309 , 34.8568 ],
[ 377.0 , 9.2243 , 34.856 ],
[ 378.0 , 9.2112 , 34.8551 ],
[ 379.0 , 9.2062 , 34.8546 ],
[ 380.0 , 9.1995 , 34.8541 ],
[ 381.0 , 9.1937 , 34.8536 ],
[ 382.0 , 9.1896 , 34.8532 ],
[ 383.0 , 9.1595 , 34.8511 ],
[ 384.0 , 9.1453 , 34.8489 ],
[ 385.0 , 9.1365 , 34.8483 ],
[ 386.0 , 9.1121 , 34.8456 ],
[ 387.0 , 9.0664 , 34.8412 ],
[ 388.0 , 9.0351 , 34.8383 ],
[ 389.0 , 9.0038 , 34.8347 ],
[ 390.0 , 8.9788 , 34.8318 ],
[ 391.0 , 8.9658 , 34.831 ],
[ 392.0 , 8.9479 , 34.829 ],
[ 393.0 , 8.9285 , 34.8259 ],
[ 394.0 , 8.9123 , 34.8228 ],
[ 395.0 , 8.8971 , 34.8208 ],
[ 396.0 , 8.8789 , 34.8181 ],
[ 397.0 , 8.8506 , 34.8144 ],
[ 398.0 , 8.8377 , 34.8128 ],
[ 399.0 , 8.8152 , 34.8105 ],
[ 400.0 , 8.783 , 34.8061 ],
[ 401.0 , 8.7541 , 34.8024 ],
[ 402.0 , 8.7252 , 34.799 ],
[ 403.0 , 8.7119 , 34.7973 ],
[ 404.0 , 8.6953 , 34.795 ],
[ 405.0 , 8.685 , 34.7934 ],
[ 406.0 , 8.6673 , 34.7909 ],
[ 407.0 , 8.6555 , 34.7896 ],
[ 408.0 , 8.63 , 34.787 ],
[ 409.0 , 8.5952 , 34.7841 ],
[ 410.0 , 8.5774 , 34.7823 ],
[ 411.0 , 8.569 , 34.7814 ],
[ 412.0 , 8.5539 , 34.7807 ],
[ 413.0 , 8.5327 , 34.7785 ],
[ 414.0 , 8.5273 , 34.7785 ],
[ 415.0 , 8.5236 , 34.7792 ],
[ 416.0 , 8.5119 , 34.7793 ],
[ 417.0 , 8.4989 , 34.7799 ],
[ 418.0 , 8.4786 , 34.7782 ],
[ 419.0 , 8.4243 , 34.7727 ],
[ 420.0 , 8.3687 , 34.7683 ],
[ 421.0 , 8.3636 , 34.7674 ],
[ 422.0 , 8.3477 , 34.7658 ],
[ 423.0 , 8.3344 , 34.7645 ],
[ 424.0 , 8.3165 , 34.7631 ],
[ 425.0 , 8.2965 , 34.7625 ],
[ 426.0 , 8.2796 , 34.7622 ],
[ 427.0 , 8.272 , 34.7621 ],
[ 428.0 , 8.2627 , 34.7624 ],
[ 429.0 , 8.2524 , 34.7635 ],
[ 430.0 , 8.2432 , 34.7636 ],
[ 431.0 , 8.2442 , 34.764 ],
[ 432.0 , 8.2448 , 34.7645 ],
[ 433.0 , 8.2448 , 34.7645 ],
[ 434.0 , 8.2413 , 34.7641 ],
[ 435.0 , 8.2462 , 34.7663 ],
[ 436.0 , 8.2633 , 34.7734 ],
[ 437.0 , 8.2674 , 34.7758 ],
[ 438.0 , 8.2671 , 34.7758 ],
[ 439.0 , 8.2664 , 34.7757 ],
[ 440.0 , 8.2658 , 34.7757 ],
[ 441.0 , 8.2655 , 34.7755 ],
[ 442.0 , 8.2655 , 34.7756 ],
[ 443.0 , 8.2656 , 34.7756 ],
[ 444.0 , 8.2639 , 34.7758 ],
[ 445.0 , 8.2578 , 34.7763 ],
[ 446.0 , 8.2561 , 34.7762 ],
[ 447.0 , 8.2519 , 34.7761 ],
[ 448.0 , 8.238 , 34.7751 ],
[ 449.0 , 8.2254 , 34.7743 ],
[ 450.0 , 8.211 , 34.773 ],
[ 451.0 , 8.2043 , 34.7724 ],
[ 452.0 , 8.1995 , 34.7722 ],
[ 453.0 , 8.1967 , 34.7722 ],
[ 454.0 , 8.1949 , 34.772 ],
[ 455.0 , 8.193 , 34.772 ],
[ 456.0 , 8.1898 , 34.7715 ],
[ 457.0 , 8.186 , 34.7714 ],
[ 458.0 , 8.1797 , 34.7711 ],
[ 459.0 , 8.1668 , 34.7696 ],
[ 460.0 , 8.1636 , 34.769 ],
[ 461.0 , 8.1421 , 34.7667 ],
[ 462.0 , 8.1183 , 34.7647 ],
[ 463.0 , 8.1081 , 34.7638 ],
[ 464.0 , 8.0935 , 34.7627 ],
[ 465.0 , 8.0706 , 34.7598 ],
[ 466.0 , 8.0642 , 34.7588 ],
[ 467.0 , 8.0555 , 34.7578 ],
[ 468.0 , 8.0402 , 34.7569 ],
[ 469.0 , 8.031 , 34.7557 ],
[ 470.0 , 8.0165 , 34.7543 ],
[ 471.0 , 8.0133 , 34.7535 ],
[ 472.0 , 7.9998 , 34.7529 ],
[ 473.0 , 7.9971 , 34.7532 ],
[ 474.0 , 7.9921 , 34.7533 ],
[ 475.0 , 7.9833 , 34.7534 ],
[ 476.0 , 7.9738 , 34.7537 ],
[ 477.0 , 7.9383 , 34.7531 ],
[ 478.0 , 7.9044 , 34.7493 ],
[ 479.0 , 7.8974 , 34.7483 ],
[ 480.0 , 7.8939 , 34.748 ],
[ 481.0 , 7.8812 , 34.7468 ],
[ 482.0 , 7.8738 , 34.7463 ],
[ 483.0 , 7.8747 , 34.7475 ],
[ 484.0 , 7.867 , 34.7478 ],
[ 485.0 , 7.8531 , 34.7475 ],
[ 486.0 , 7.8455 , 34.7466 ],
[ 487.0 , 7.8403 , 34.7465 ],
[ 488.0 , 7.8477 , 34.7507 ],
[ 489.0 , 7.8438 , 34.7503 ],
[ 490.0 , 7.8377 , 34.7498 ],
[ 491.0 , 7.8287 , 34.7491 ],
[ 492.0 , 7.822 , 34.7482 ],
[ 493.0 , 7.8139 , 34.7474 ],
[ 494.0 , 7.806 , 34.7466 ],
[ 495.0 , 7.784 , 34.7444 ],
[ 496.0 , 7.762 , 34.7417 ],
[ 497.0 , 7.7472 , 34.7401 ],
[ 498.0 , 7.6989 , 34.7368 ],
[ 499.0 , 7.6625 , 34.7326 ],
[ 500.0 , 7.6478 , 34.7303 ],
[ 501.0 , 7.6308 , 34.7278 ],
[ 502.0 , 7.5919 , 34.7238 ],
[ 503.0 , 7.5723 , 34.7218 ],
[ 504.0 , 7.553 , 34.7207 ],
[ 505.0 , 7.5091 , 34.7178 ],
[ 506.0 , 7.4825 , 34.7143 ],
[ 507.0 , 7.4758 , 34.7129 ],
[ 508.0 , 7.4593 , 34.7105 ],
[ 509.0 , 7.4453 , 34.7088 ],
[ 510.0 , 7.4306 , 34.7072 ],
[ 511.0 , 7.4226 , 34.7061 ],
[ 512.0 , 7.4118 , 34.7047 ],
[ 513.0 , 7.4064 , 34.704 ],
[ 514.0 , 7.4014 , 34.7036 ],
[ 515.0 , 7.3742 , 34.7005 ],
[ 516.0 , 7.3163 , 34.694 ],
[ 517.0 , 7.2944 , 34.6919 ],
[ 518.0 , 7.2741 , 34.6892 ],
[ 519.0 , 7.2611 , 34.6871 ],
[ 520.0 , 7.241 , 34.6852 ],
[ 521.0 , 7.2164 , 34.6831 ],
[ 522.0 , 7.1888 , 34.6801 ],
[ 523.0 , 7.1824 , 34.6794 ],
[ 524.0 , 7.164 , 34.6781 ],
[ 525.0 , 7.1393 , 34.6753 ],
[ 526.0 , 7.1139 , 34.6726 ],
[ 527.0 , 7.1027 , 34.6704 ],
[ 528.0 , 7.0975 , 34.6697 ],
[ 529.0 , 7.0893 , 34.6691 ],
[ 530.0 , 7.0866 , 34.6694 ],
[ 531.0 , 7.0614 , 34.6674 ],
[ 532.0 , 7.0483 , 34.6646 ],
[ 533.0 , 7.0309 , 34.6638 ],
[ 534.0 , 7.0314 , 34.6636 ],
[ 535.0 , 7.0224 , 34.6631 ],
[ 536.0 , 7.0141 , 34.6613 ],
[ 537.0 , 7.0075 , 34.6604 ],
[ 538.0 , 6.9998 , 34.6598 ],
[ 539.0 , 6.9861 , 34.659 ],
[ 540.0 , 6.9793 , 34.6586 ],
[ 541.0 , 6.9848 , 34.6599 ],
[ 542.0 , 6.9907 , 34.6617 ],
[ 543.0 , 6.9952 , 34.6633 ],
[ 544.0 , 6.9827 , 34.6637 ],
[ 545.0 , 6.9482 , 34.6607 ],
[ 546.0 , 6.9366 , 34.6574 ],
[ 547.0 , 6.9206 , 34.6548 ],
[ 548.0 , 6.9094 , 34.6536 ],
[ 549.0 , 6.8957 , 34.6522 ],
[ 550.0 , 6.8774 , 34.6506 ],
[ 551.0 , 6.8654 , 34.6492 ],
[ 552.0 , 6.8539 , 34.6478 ],
[ 553.0 , 6.8402 , 34.6462 ],
[ 554.0 , 6.8135 , 34.6456 ],
[ 555.0 , 6.7682 , 34.6405 ],
[ 556.0 , 6.7476 , 34.6347 ],
[ 557.0 , 6.7272 , 34.6334 ],
[ 558.0 , 6.7187 , 34.6323 ],
[ 559.0 , 6.7117 , 34.6315 ],
[ 560.0 , 6.7039 , 34.6305 ],
[ 561.0 , 6.6987 , 34.6301 ],
[ 562.0 , 6.6925 , 34.6298 ],
[ 563.0 , 6.688 , 34.6297 ],
[ 564.0 , 6.6825 , 34.6291 ],
[ 565.0 , 6.6752 , 34.6281 ],
[ 566.0 , 6.6643 , 34.6271 ],
[ 567.0 , 6.6533 , 34.6261 ],
[ 568.0 , 6.6373 , 34.6245 ],
[ 569.0 , 6.6191 , 34.6231 ],
[ 570.0 , 6.6085 , 34.6221 ],
[ 571.0 , 6.5927 , 34.6214 ],
[ 572.0 , 6.5664 , 34.6195 ],
[ 573.0 , 6.5574 , 34.6183 ],
[ 574.0 , 6.5536 , 34.6177 ],
[ 575.0 , 6.5501 , 34.6172 ],
[ 576.0 , 6.5422 , 34.6166 ],
[ 577.0 , 6.5278 , 34.6152 ],
[ 578.0 , 6.5148 , 34.614 ],
[ 579.0 , 6.5112 , 34.6137 ],
[ 580.0 , 6.5046 , 34.6133 ],
[ 581.0 , 6.486 , 34.6129 ],
[ 582.0 , 6.4477 , 34.6096 ],
[ 583.0 , 6.4375 , 34.6074 ],
[ 584.0 , 6.4156 , 34.6053 ],
[ 585.0 , 6.3959 , 34.6042 ],
[ 586.0 , 6.3791 , 34.6027 ],
[ 587.0 , 6.3729 , 34.6018 ],
[ 588.0 , 6.3694 , 34.6014 ],
[ 589.0 , 6.3672 , 34.6013 ],
[ 590.0 , 6.3645 , 34.6012 ],
[ 591.0 , 6.3624 , 34.6012 ],
[ 592.0 , 6.3614 , 34.6012 ],
[ 593.0 , 6.3549 , 34.6005 ],
[ 594.0 , 6.3406 , 34.5992 ],
[ 595.0 , 6.3207 , 34.5978 ],
[ 596.0 , 6.308 , 34.5968 ],
[ 597.0 , 6.3031 , 34.5964 ],
[ 598.0 , 6.2967 , 34.5961 ],
[ 599.0 , 6.2898 , 34.5957 ],
[ 600.0 , 6.2827 , 34.5953 ],
[ 601.0 , 6.2774 , 34.5953 ],
[ 602.0 , 6.2678 , 34.5947 ],
[ 603.0 , 6.2614 , 34.5944 ],
[ 604.0 , 6.26 , 34.5941 ],
[ 605.0 , 6.2587 , 34.594 ],
[ 606.0 , 6.2588 , 34.5941 ],
[ 607.0 , 6.2591 , 34.5943 ],
[ 608.0 , 6.2557 , 34.5944 ],
[ 609.0 , 6.2426 , 34.5935 ],
[ 610.0 , 6.2304 , 34.5922 ],
[ 611.0 , 6.22 , 34.591 ],
[ 612.0 , 6.2184 , 34.591 ],
[ 613.0 , 6.2144 , 34.5907 ],
[ 614.0 , 6.1981 , 34.5893 ],
[ 615.0 , 6.1862 , 34.5886 ],
[ 616.0 , 6.1764 , 34.588 ],
[ 617.0 , 6.1659 , 34.5872 ],
[ 618.0 , 6.1566 , 34.5858 ],
[ 619.0 , 6.1476 , 34.5847 ],
[ 620.0 , 6.1443 , 34.5845 ],
[ 621.0 , 6.14 , 34.5841 ],
[ 622.0 , 6.1162 , 34.5821 ],
[ 623.0 , 6.1183 , 34.5826 ],
[ 624.0 , 6.1171 , 34.5823 ],
[ 625.0 , 6.1044 , 34.5821 ],
[ 626.0 , 6.0618 , 34.5785 ],
[ 627.0 , 6.0414 , 34.5768 ],
[ 628.0 , 6.0366 , 34.5765 ],
[ 629.0 , 6.0356 , 34.5765 ],
[ 630.0 , 6.0342 , 34.5768 ],
[ 631.0 , 6.0328 , 34.5766 ],
[ 632.0 , 6.0303 , 34.5765 ],
[ 633.0 , 6.0167 , 34.5757 ],
[ 634.0 , 6.0014 , 34.5748 ],
[ 635.0 , 5.9903 , 34.574 ],
[ 636.0 , 5.9862 , 34.5736 ],
[ 637.0 , 5.9839 , 34.5736 ],
[ 638.0 , 5.9826 , 34.5735 ],
[ 639.0 , 5.982 , 34.5735 ],
[ 640.0 , 5.9806 , 34.5736 ],
[ 641.0 , 5.9795 , 34.5733 ],
[ 642.0 , 5.9781 , 34.5732 ],
[ 643.0 , 5.9765 , 34.5734 ],
[ 644.0 , 5.9636 , 34.5731 ],
[ 645.0 , 5.9544 , 34.5721 ],
[ 646.0 , 5.9502 , 34.5715 ],
[ 647.0 , 5.9483 , 34.5716 ],
[ 648.0 , 5.9406 , 34.5713 ],
[ 649.0 , 5.928 , 34.5705 ],
[ 650.0 , 5.9258 , 34.5701 ],
[ 651.0 , 5.9221 , 34.5698 ],
[ 652.0 , 5.9146 , 34.5694 ],
[ 653.0 , 5.9066 , 34.5689 ],
[ 654.0 , 5.9039 , 34.5688 ],
[ 655.0 , 5.9018 , 34.5685 ],
[ 656.0 , 5.8994 , 34.5688 ],
[ 657.0 , 5.8982 , 34.5684 ],
[ 658.0 , 5.8945 , 34.5686 ],
[ 659.0 , 5.8915 , 34.5682 ],
[ 660.0 , 5.8876 , 34.5679 ],
[ 661.0 , 5.8828 , 34.5679 ],
[ 662.0 , 5.8783 , 34.5677 ],
[ 663.0 , 5.874 , 34.5674 ],
[ 664.0 , 5.8698 , 34.5668 ],
[ 665.0 , 5.8657 , 34.5666 ],
[ 666.0 , 5.8622 , 34.5668 ],
[ 667.0 , 5.8516 , 34.5667 ],
[ 668.0 , 5.8475 , 34.566 ],
[ 669.0 , 5.8427 , 34.5658 ],
[ 670.0 , 5.8379 , 34.5655 ],
[ 671.0 , 5.8359 , 34.566 ],
[ 672.0 , 5.8261 , 34.5658 ],
[ 673.0 , 5.819 , 34.5652 ],
[ 674.0 , 5.8144 , 34.5647 ],
[ 675.0 , 5.8116 , 34.5646 ],
[ 676.0 , 5.8111 , 34.5645 ],
[ 677.0 , 5.8103 , 34.5645 ],
[ 678.0 , 5.8104 , 34.5647 ],
[ 679.0 , 5.8097 , 34.5647 ],
[ 680.0 , 5.8078 , 34.5647 ],
[ 681.0 , 5.7942 , 34.5647 ],
[ 682.0 , 5.7681 , 34.563 ],
[ 683.0 , 5.737 , 34.5614 ],
[ 684.0 , 5.7295 , 34.562 ],
[ 685.0 , 5.7199 , 34.5613 ],
[ 686.0 , 5.7173 , 34.5612 ],
[ 687.0 , 5.717 , 34.5611 ],
[ 688.0 , 5.7142 , 34.5614 ],
[ 689.0 , 5.7122 , 34.5613 ],
[ 690.0 , 5.7126 , 34.5614 ],
[ 691.0 , 5.7099 , 34.5614 ],
[ 692.0 , 5.7053 , 34.5614 ],
[ 693.0 , 5.7036 , 34.5614 ],
[ 694.0 , 5.7022 , 34.5614 ],
[ 695.0 , 5.6971 , 34.561 ],
[ 696.0 , 5.6904 , 34.5609 ],
[ 697.0 , 5.6868 , 34.5606 ],
[ 698.0 , 5.6843 , 34.5606 ],
[ 699.0 , 5.6741 , 34.5605 ],
[ 700.0 , 5.6551 , 34.5593 ],
[ 701.0 , 5.6406 , 34.5583 ],
[ 702.0 , 5.635 , 34.5575 ],
[ 703.0 , 5.6244 , 34.5565 ],
[ 704.0 , 5.6175 , 34.5563 ],
[ 705.0 , 5.6139 , 34.5561 ],
[ 706.0 , 5.6122 , 34.556 ],
[ 707.0 , 5.6111 , 34.5564 ],
[ 708.0 , 5.6009 , 34.5565 ],
[ 709.0 , 5.5935 , 34.5571 ],
[ 710.0 , 5.577 , 34.5568 ],
[ 711.0 , 5.5692 , 34.556 ],
[ 712.0 , 5.5683 , 34.5554 ],
[ 713.0 , 5.5641 , 34.5554 ],
[ 714.0 , 5.5579 , 34.5552 ],
[ 715.0 , 5.5539 , 34.5552 ],
[ 716.0 , 5.5508 , 34.5553 ],
[ 717.0 , 5.547 , 34.5554 ],
[ 718.0 , 5.5354 , 34.5548 ],
[ 719.0 , 5.5047 , 34.5534 ],
[ 720.0 , 5.4831 , 34.5526 ],
[ 721.0 , 5.4715 , 34.552 ],
[ 722.0 , 5.4631 , 34.5516 ],
[ 723.0 , 5.4513 , 34.551 ],
[ 724.0 , 5.4411 , 34.5508 ],
[ 725.0 , 5.4174 , 34.5508 ],
[ 726.0 , 5.4122 , 34.5506 ],
[ 727.0 , 5.4119 , 34.5506 ],
[ 728.0 , 5.4106 , 34.551 ],
[ 729.0 , 5.4112 , 34.5511 ],
[ 730.0 , 5.4109 , 34.5512 ],
[ 731.0 , 5.411 , 34.5517 ],
[ 732.0 , 5.4103 , 34.5516 ],
[ 733.0 , 5.4019 , 34.5518 ],
[ 734.0 , 5.3702 , 34.5517 ],
[ 735.0 , 5.3565 , 34.5511 ],
[ 736.0 , 5.3549 , 34.551 ],
[ 737.0 , 5.3543 , 34.5512 ],
[ 738.0 , 5.3536 , 34.5514 ],
[ 739.0 , 5.3522 , 34.5515 ],
[ 740.0 , 5.3498 , 34.5517 ],
[ 741.0 , 5.3484 , 34.552 ],
[ 742.0 , 5.3468 , 34.5519 ],
[ 743.0 , 5.3445 , 34.5519 ],
[ 744.0 , 5.3428 , 34.5519 ],
[ 745.0 , 5.3402 , 34.552 ],
[ 746.0 , 5.3371 , 34.552 ],
[ 747.0 , 5.3329 , 34.5521 ],
[ 748.0 , 5.3262 , 34.552 ],
[ 749.0 , 5.3182 , 34.5518 ],
[ 750.0 , 5.304 , 34.5519 ],
[ 751.0 , 5.2914 , 34.552 ],
[ 752.0 , 5.2859 , 34.5521 ],
[ 753.0 , 5.2734 , 34.5519 ],
[ 754.0 , 5.2654 , 34.5517 ],
[ 755.0 , 5.2527 , 34.552 ],
[ 756.0 , 5.2468 , 34.5521 ],
[ 757.0 , 5.2399 , 34.5524 ],
[ 758.0 , 5.2321 , 34.5522 ],
[ 759.0 , 5.2262 , 34.5517 ],
[ 760.0 , 5.2131 , 34.5521 ],
[ 761.0 , 5.2087 , 34.5521 ],
[ 762.0 , 5.2097 , 34.5519 ],
[ 763.0 , 5.1968 , 34.5525 ],
[ 764.0 , 5.1745 , 34.5534 ],
[ 765.0 , 5.1679 , 34.5534 ],
[ 766.0 , 5.1656 , 34.553 ],
[ 767.0 , 5.1518 , 34.5536 ],
[ 768.0 , 5.151 , 34.5537 ],
[ 769.0 , 5.1494 , 34.5536 ],
[ 770.0 , 5.1451 , 34.5537 ],
[ 771.0 , 5.1349 , 34.5545 ],
[ 772.0 , 5.1291 , 34.5548 ],
[ 773.0 , 5.1278 , 34.5545 ],
[ 774.0 , 5.1267 , 34.5547 ],
[ 775.0 , 5.1264 , 34.5545 ],
[ 776.0 , 5.1245 , 34.5551 ],
[ 777.0 , 5.1242 , 34.5551 ],
[ 778.0 , 5.1225 , 34.5555 ],
[ 779.0 , 5.1216 , 34.5558 ],
[ 780.0 , 5.1205 , 34.5562 ],
[ 781.0 , 5.1174 , 34.5565 ],
[ 782.0 , 5.1141 , 34.5566 ],
[ 783.0 , 5.1085 , 34.5573 ],
[ 784.0 , 5.1072 , 34.5572 ],
[ 785.0 , 5.1033 , 34.5574 ],
[ 786.0 , 5.0943 , 34.5574 ],
[ 787.0 , 5.0867 , 34.5576 ],
[ 788.0 , 5.079 , 34.5581 ],
[ 789.0 , 5.0736 , 34.5583 ],
[ 790.0 , 5.0722 , 34.5583 ],
[ 791.0 , 5.0707 , 34.5583 ],
[ 792.0 , 5.066 , 34.5587 ],
[ 793.0 , 5.0608 , 34.5594 ],
[ 794.0 , 5.0588 , 34.5592 ],
[ 795.0 , 5.0517 , 34.5598 ],
[ 796.0 , 5.0371 , 34.5609 ],
[ 797.0 , 5.0256 , 34.5621 ],
[ 798.0 , 5.0206 , 34.5625 ],
[ 799.0 , 5.0177 , 34.5628 ],
[ 800.0 , 5.0138 , 34.5631 ],
[ 801.0 , 5.0078 , 34.5635 ],
[ 802.0 , 5.0046 , 34.5637 ],
[ 803.0 , 5.0016 , 34.5641 ],
[ 804.0 , 5.0004 , 34.5644 ],
[ 805.0 , 4.9985 , 34.5648 ],
[ 806.0 , 4.9962 , 34.5649 ],
[ 807.0 , 4.9912 , 34.5655 ],
[ 808.0 , 4.984 , 34.5664 ],
[ 809.0 , 4.9825 , 34.5666 ],
[ 810.0 , 4.982 , 34.5669 ],
[ 811.0 , 4.9801 , 34.567 ],
[ 812.0 , 4.977 , 34.5675 ],
[ 813.0 , 4.9758 , 34.5676 ],
[ 814.0 , 4.9753 , 34.5678 ],
[ 815.0 , 4.9727 , 34.5683 ],
[ 816.0 , 4.971 , 34.5687 ],
[ 817.0 , 4.9696 , 34.5691 ],
[ 818.0 , 4.967 , 34.5697 ],
[ 819.0 , 4.9639 , 34.5701 ],
[ 820.0 , 4.9625 , 34.5707 ],
[ 821.0 , 4.9596 , 34.5713 ],
[ 822.0 , 4.9574 , 34.5716 ],
[ 823.0 , 4.9549 , 34.572 ],
[ 824.0 , 4.9509 , 34.5719 ],
[ 825.0 , 4.9413 , 34.5728 ],
[ 826.0 , 4.9281 , 34.5744 ],
[ 827.0 , 4.9274 , 34.5743 ],
[ 828.0 , 4.9271 , 34.5742 ],
[ 829.0 , 4.9262 , 34.5745 ],
[ 830.0 , 4.922 , 34.5753 ],
[ 831.0 , 4.9171 , 34.5762 ],
[ 832.0 , 4.9145 , 34.5765 ],
[ 833.0 , 4.9122 , 34.5768 ],
[ 834.0 , 4.9108 , 34.577 ],
[ 835.0 , 4.9084 , 34.5773 ],
[ 836.0 , 4.9067 , 34.5776 ],
[ 837.0 , 4.9039 , 34.5779 ],
[ 838.0 , 4.9001 , 34.5785 ],
[ 839.0 , 4.8925 , 34.5793 ],
[ 840.0 , 4.8864 , 34.5801 ],
[ 841.0 , 4.8799 , 34.581 ],
[ 842.0 , 4.8674 , 34.584 ],
[ 843.0 , 4.8609 , 34.5856 ],
[ 844.0 , 4.8589 , 34.5857 ],
[ 845.0 , 4.8556 , 34.5863 ],
[ 846.0 , 4.8535 , 34.5868 ],
[ 847.0 , 4.8509 , 34.5878 ],
[ 848.0 , 4.848 , 34.5885 ],
[ 849.0 , 4.8461 , 34.589 ],
[ 850.0 , 4.8448 , 34.5892 ],
[ 851.0 , 4.8437 , 34.5894 ],
[ 852.0 , 4.8423 , 34.5897 ],
[ 853.0 , 4.8415 , 34.59 ],
[ 854.0 , 4.8405 , 34.5906 ],
[ 855.0 , 4.8386 , 34.5914 ],
[ 856.0 , 4.837 , 34.5914 ],
[ 857.0 , 4.8359 , 34.5916 ],
[ 858.0 , 4.8311 , 34.5927 ],
[ 859.0 , 4.8266 , 34.5942 ],
[ 860.0 , 4.8229 , 34.5955 ],
[ 861.0 , 4.8186 , 34.5967 ],
[ 862.0 , 4.8149 , 34.5972 ],
[ 863.0 , 4.8109 , 34.5975 ],
[ 864.0 , 4.8064 , 34.5979 ],
[ 865.0 , 4.805 , 34.5984 ],
[ 866.0 , 4.8021 , 34.5991 ],
[ 867.0 , 4.7957 , 34.6011 ],
[ 868.0 , 4.7926 , 34.6018 ],
[ 869.0 , 4.7927 , 34.6031 ],
[ 870.0 , 4.7909 , 34.6031 ],
[ 871.0 , 4.7861 , 34.603 ],
[ 872.0 , 4.7868 , 34.6038 ],
[ 873.0 , 4.7837 , 34.6036 ],
[ 874.0 , 4.782 , 34.6033 ],
[ 875.0 , 4.7798 , 34.6035 ],
[ 876.0 , 4.7802 , 34.6039 ],
[ 877.0 , 4.7798 , 34.604 ],
[ 878.0 , 4.7792 , 34.6043 ],
[ 879.0 , 4.7789 , 34.6044 ],
[ 880.0 , 4.7788 , 34.605 ],
[ 881.0 , 4.7791 , 34.6052 ],
[ 882.0 , 4.7787 , 34.6055 ],
[ 883.0 , 4.7785 , 34.6055 ],
[ 884.0 , 4.778 , 34.6058 ],
[ 885.0 , 4.7778 , 34.6059 ],
[ 886.0 , 4.7776 , 34.6059 ],
[ 887.0 , 4.7766 , 34.607 ],
[ 888.0 , 4.7754 , 34.6078 ],
[ 889.0 , 4.7752 , 34.6079 ],
[ 890.0 , 4.7748 , 34.609 ],
[ 891.0 , 4.7733 , 34.6109 ],
[ 892.0 , 4.7705 , 34.6127 ],
[ 893.0 , 4.7674 , 34.6142 ],
[ 894.0 , 4.7658 , 34.6154 ],
[ 895.0 , 4.7656 , 34.6156 ],
[ 896.0 , 4.7639 , 34.6172 ],
[ 897.0 , 4.7632 , 34.6175 ],
[ 898.0 , 4.763 , 34.6174 ],
[ 899.0 , 4.7625 , 34.618 ],
[ 900.0 , 4.7615 , 34.6184 ],
[ 901.0 , 4.7604 , 34.619 ],
[ 902.0 , 4.7592 , 34.6196 ],
[ 903.0 , 4.7584 , 34.6202 ],
[ 904.0 , 4.7572 , 34.6208 ],
[ 905.0 , 4.756 , 34.6211 ],
[ 906.0 , 4.755 , 34.6214 ],
[ 907.0 , 4.7509 , 34.6233 ],
[ 908.0 , 4.7451 , 34.6264 ],
[ 909.0 , 4.7422 , 34.6276 ],
[ 910.0 , 4.7408 , 34.6283 ],
[ 911.0 , 4.7406 , 34.6286 ],
[ 912.0 , 4.7404 , 34.629 ],
[ 913.0 , 4.7394 , 34.6292 ],
[ 914.0 , 4.7378 , 34.6291 ],
[ 915.0 , 4.7358 , 34.6292 ],
[ 916.0 , 4.7333 , 34.6292 ],
[ 917.0 , 4.7313 , 34.6297 ],
[ 918.0 , 4.73 , 34.6306 ],
[ 919.0 , 4.7286 , 34.6313 ],
[ 920.0 , 4.7284 , 34.6313 ],
[ 921.0 , 4.7283 , 34.6317 ],
[ 922.0 , 4.7276 , 34.6322 ],
[ 923.0 , 4.7277 , 34.6323 ],
[ 924.0 , 4.727 , 34.6341 ],
[ 925.0 , 4.7303 , 34.6392 ],
[ 926.0 , 4.7327 , 34.6411 ],
[ 927.0 , 4.7315 , 34.641 ],
[ 928.0 , 4.7314 , 34.6412 ],
[ 929.0 , 4.7304 , 34.6414 ],
[ 930.0 , 4.7297 , 34.642 ],
[ 931.0 , 4.7294 , 34.6424 ],
[ 932.0 , 4.7283 , 34.6424 ],
[ 933.0 , 4.728 , 34.6429 ],
[ 934.0 , 4.7281 , 34.6436 ],
[ 935.0 , 4.7265 , 34.6436 ],
[ 936.0 , 4.7258 , 34.6436 ],
[ 937.0 , 4.7258 , 34.6442 ],
[ 938.0 , 4.7246 , 34.6446 ],
[ 939.0 , 4.7217 , 34.6444 ],
[ 940.0 , 4.7206 , 34.6448 ],
[ 941.0 , 4.7197 , 34.6451 ],
[ 942.0 , 4.7198 , 34.6454 ],
[ 943.0 , 4.7194 , 34.646 ],
[ 944.0 , 4.7197 , 34.6472 ],
[ 945.0 , 4.7191 , 34.6478 ],
[ 946.0 , 4.7208 , 34.6488 ],
[ 947.0 , 4.7233 , 34.6492 ],
[ 948.0 , 4.7258 , 34.6503 ],
[ 949.0 , 4.73 , 34.6511 ],
[ 950.0 , 4.7356 , 34.6526 ],
[ 951.0 , 4.7402 , 34.6534 ],
[ 952.0 , 4.7476 , 34.6547 ],
[ 953.0 , 4.7514 , 34.6558 ],
[ 954.0 , 4.7512 , 34.6561 ],
[ 955.0 , 4.7503 , 34.6559 ],
[ 956.0 , 4.7493 , 34.6556 ],
[ 957.0 , 4.7456 , 34.6551 ],
[ 958.0 , 4.7409 , 34.6549 ],
[ 959.0 , 4.7439 , 34.6558 ],
[ 960.0 , 4.75 , 34.6579 ],
[ 961.0 , 4.7514 , 34.6588 ],
[ 962.0 , 4.7516 , 34.6593 ],
[ 963.0 , 4.7485 , 34.6591 ],
[ 964.0 , 4.7445 , 34.6591 ],
[ 965.0 , 4.7407 , 34.6617 ],
[ 966.0 , 4.3749 , 35.0292 ],
[ 967.0 , -0.1451 , 40.2138 ],
[ 968.0 , -14.7062 , 68.6005 ],
[ 969.0 , 4.8179 , 34.751 ],
[ 970.0 , 4.7111 , 34.8372 ],
[ 971.0 , 4.7078 , 34.8167 ],
[ 972.0 , 4.7072 , 34.7578 ],
[ 973.0 , 4.7082 , 34.7463 ],
[ 974.0 , 4.7087 , 34.7381 ],
[ 975.0 , 4.7093 , 34.73 ],
[ 976.0 , 4.71 , 34.722 ],
[ 977.0 , -5.8982 , 48.7891 ],
[ 978.0 , -20.5277 , 88.9406 ],
[ 979.0 , -12.8455 , 64.0201 ],
[ 980.0 , 6.039 , 33.73 ],
[ 981.0 , 1.9029 , 38.0616 ],
[ 982.0 , -7.7971 , 52.6434 ],
[ 983.0 , 27.6694 , 20.1979 ],
[ 984.0 , 10.6719 , 30.0656 ],
[ 985.0 , 0.774 , 40.1519 ],
[ 986.0 , 1.225 , 40.0327 ],
[ 987.0 , 29.6521 , 20.369 ],
[ 988.0 , -1.6783 , 45.4642 ],
[ 989.0 , 4.0463 , 37.8228 ],
[ 990.0 , 0.9936 , 40.9515 ],
[ 991.0 , 3.6411 , 37.483 ],
[ 992.0 , 1.0686 , 40.4812 ],
[ 993.0 , 4.5737 , 36.2241 ],
[ 994.0 , 4.7179 , 35.815 ],
[ 995.0 , 4.7252 , 35.5623 ],
[ 996.0 , 4.4075 , 35.8497 ],
[ 997.0 , -22.9845 , 102.4913 ],
[ 998.0 , 48.2096 , 14.6565 ],
[ 999.0 , 98.0594 , 8.4699 ],
[ 1000.0 , 53.171 , 13.5008 ],
[ 1001.0 , -7.3098 , 52.4037 ],
[ 1002.0 , -17.3948 , 78.5884 ],
[ 1003.0 , 12.4177 , 28.6903 ],
[ 1004.0 , 1.6885 , 39.4541 ],
[ 1005.0 , 3.3362 , 37.3498 ],
[ 1006.0 , 4.7036 , 35.8165 ],
[ 1007.0 , 4.7056 , 35.6839 ],
[ 1008.0 , 4.7071 , 35.473 ],
[ 1009.0 , 4.7061 , 35.2114 ],
[ 1010.0 , 2.2747 , 37.7876 ],
[ 1011.0 , 48.6645 , 14.2963 ],
[ 1012.0 , 98.4519 , 8.2849 ],
[ 1013.0 , 39.1868 , 16.8033 ],
[ 1014.0 , -19.3419 , 91.0774 ]])
p = util.testingProfile.fakeProfile(data[:, 1], 
                                    data[:, 0], 
                                    salinities = data[:, 2],
                                    latitude   = 4.10566666667,
                                    longitude  = -38.0133333333,
                                    date       = [2008, 04, 17, 0.94361111]) 

expected_qc_anomaly_detection = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, True, True, True, True, True, False, True, True, True, False, False, True, True, True, True, False, True, False, False, False, False, True, True, True, True, True, True, True, True, False, False, False, False, False, True, True, True, False, False]



