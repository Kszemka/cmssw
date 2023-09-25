from typing import List, Tuple
from datetime import datetime
import time

def to_unix_timestamp(date_string):
    date_format = "%d/%m/%Y %H:%M:%S"
    datetime_obj = datetime.strptime(date_string, date_format)
    unix_timestamp = int(time.mktime(datetime_obj.timetuple()))
    return unix_timestamp


def to_date_string(unix_timestamp):
    datetime_obj = datetime.fromtimestamp(unix_timestamp)
    date_string = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")
    return date_string

def read_split(file) -> Tuple[str, List[str]]:
    line = file.readline()
    return line, line.split(";")

# def print_class(line_pps: str, split_pps: List[str], line_cls: str, split_cls: List[str],
#                 time_ix: int, ls_ix: int, to_print: List[int], print_date: bool = True):
#     if(len(split_pps) > 5 and len(split_cls) > max()):
#         # if len(split_pps[5][1:-1]) != len('17/04/2023 07:30:42'):
#         #     print(split_pps[5][1:-1], len(split_pps[5][1:-1]), len('17/04/2023 07:30:42'))
#         #     print(split_pps[5][1:-1])
#         #     print('17/04/2023 07:30:42')
#         #     exit(0)
#         pps_timestamp = to_unix_timestamp(split_pps[5][1:-1]) + 2*60*60 # - coversion of time zones
#         # print(pps_timestamp, "-", int(split_cls[2]), "=", pps_timestamp -int(split_cls[2]), end = " |; ")
#         if(abs(pps_timestamp-int(split_cls[2])) < 10*60 and split_pps[2] == split_cls[3]):
#             # print(line_cls, end="")
#             print(split_cls[1], split_cls[3], split_cls[5], split_cls[4], split_cls[6],
#                 split_cls[0], to_date_string(int(split_cls[2])), sep=";", end=";")
#             cls_beta = float(split_cls[5])
#             cls_xangle = float(split_cls[4])

#             line_cls = f_cls.readline()
#             split_cls = line_cls.split(';')
#         else:
#             # print(";;;;;;;", end = "")
#             print(";;;;;;;                                                            ", end = "")


def main():
    # with open('8614_pps.txt') as f_pps:
    with open('9019_pps.txt') as f_pps:
        # with open('9019_content_csv_ext_filter.csv') as f_lhc:
        with open('9019_fixed_content.csv') as f_lhc:
            # with open('8614_ls_content_csv.out') as f_perls:
            with open('9019_ls_content.csv') as f_perls:
                print("fill", "pps run", "pps LS", "pps beta*", "pps xangle", "pps dip date", 
                    "record", "LS LHCInfo", "beta* LHCInfo", "xangle LHCInfo", "delivLumi LHCInfo", "IOV LHCInfo", "IOV date LHCInfo",
                    "beta* |pps-LHCInfo| error", "xangle |pps-LHCInfo| error",
                    "record", "LS PerLS", "beta*X", "beta*Y", "xangleX", "xangleY", "IOV PerLS", "IOV date PerLS",
                    "beta*X |pps-PerLS| error", "xangleX |pps-PerLS| error",
                    "", sep = ";")

                lhc_beta = None
                lhc_xangle = None
                perls_beta = None
                perls_xangle = None

                line_lhc, split_lhc = read_split(f_lhc)
                #skip the headers
                if "IOV" in line_lhc or line_lhc == "\n":
                    # print("skipping the header") #TODO remove
                    line_lhc, split_lhc = read_split(f_lhc)

                line_perls, split_perls = read_split(f_perls)
                #skip the headers
                if "IOV" in line_perls or line_perls == "\n":
                    # print("skipping the header") #TODO remove
                    line_perls, split_perls = read_split(f_perls)


                for line_pps in f_pps:
                    line_pps = line_pps[1:-2]
                    split_pps = line_pps.split(', ')

                    for i, val in enumerate(split_pps):
                        print(val, end = ";" if i <= 5 or i == len(split_pps)-1 else ", ")
                    

                    print_lhc = False
                    print_perls = False
                    # print("  pps:", (split_pps[2]), "lhc:", (split_lhc[2]))
                    if(len(split_pps) > 5 and len(split_lhc) > 5):
                        # if len(split_pps[5][1:-1]) != len('17/04/2023 07:30:42'):
                        #     print(split_pps[5][1:-1], len(split_pps[5][1:-1]), len('17/04/2023 07:30:42'))
                        #     print(split_pps[5][1:-1])
                        #     print('17/04/2023 07:30:42')
                        #     exit(0)
                        pps_timestamp = to_unix_timestamp(split_pps[5][1:-1]) + 2*60*60 # - coversion of time zones
                        # print(pps_timestamp, "-", int(split_lhc[2]), "=", pps_timestamp -int(split_lhc[2]), end = " |; ")
                        if(abs(pps_timestamp-int(split_lhc[2])) < 10*60 and split_pps[2] == split_lhc[3]):
                            # print(line_lhc, end="")
                            print(split_lhc[1], split_lhc[3], split_lhc[5], split_lhc[4], split_lhc[6],
                                split_lhc[0], to_date_string(int(split_lhc[2])), sep=";", end=";")
                            while(len(split_lhc) > 5 and abs(pps_timestamp-int(split_lhc[2])) < 10*60 and split_pps[2] == split_lhc[3]):
                                lhc_beta = float(split_lhc[5])
                                lhc_xangle = float(split_lhc[4])
                                line_lhc, split_lhc = read_split(f_lhc)
                        else:
                            # print(";;;;;;;", end = "")
                            print(";;;;;;;                                                            ", end = "")
                            print_lhc = True
                        
                    #                 lhc_beta = lhc_beta
                    # lhc_xangle = lhc_xangle
                        pps_beta = float(split_pps[3])
                        pps_xangle = float(split_pps[4])
                        # print(pps_beta, lhc_beta, pps_xangle, lhc_xangle, sep=" - ", end = " | ")
                        print(abs(pps_beta-lhc_beta) if lhc_beta is not None else 0,
                            abs(pps_xangle-lhc_xangle) if lhc_xangle is not None else 0, sep = ";", end = ";")
                    else:
                        print(";;;;;;;;;", end = "")

                    time_ix_ls = 2
                    ls_ix_ls = 4
                    run_ix_ls = 3
                    beta_ix_ls = 7
                    xangle_ix_ls = 5
                    if(len(split_pps) > 5 and len(split_perls) > max(time_ix_ls, ls_ix_ls, run_ix_ls, beta_ix_ls, xangle_ix_ls)):
                        if(split_pps[1] == split_perls[run_ix_ls] and split_pps[2] == split_perls[ls_ix_ls]):
                            # print(line_perls, end="")
                            print(split_perls[1], split_perls[4], split_perls[7], split_perls[8], split_perls[5], split_perls[6],
                                split_perls[0], to_date_string(int(split_perls[time_ix_ls])), sep=";", end=";")
                            perls_beta = float(split_perls[beta_ix_ls])
                            perls_xangle = float(split_perls[xangle_ix_ls])

                            line_perlsm, split_perls = read_split(f_perls)
                        else:
                            # print(";;;;;;;", end = "")
                            print(";;;;;;;;                                                            ", end = "")
                            print_perls = True
                        
                    #                 perls_beta = perls_beta
                    # perls_xangle = perls_xangle
                        pps_beta = float(split_pps[3])
                        pps_xangle = float(split_pps[4])
                        # print(pps_beta, perls_beta, pps_xangle, perls_xangle, sep=" - ", end = " | ")
                        print(abs(pps_beta-perls_beta) if perls_beta is not None else 0,
                            abs(pps_xangle-perls_xangle) if perls_xangle is not None else 0, sep = ";", end = ";\n")
                    else:
                        print(";;;;;;;;;;")#, end = "")
                        # print(line_perls)
                    # print(split_perls)

                    # if print_lhc:
                    #     print(line_lhc, end = "")
                    # if print_perls:
                    #     print(line_perls, end = "")
                    
                    

if __name__ == "__main__":
    main()



# 9019;369956;337;0.52;149;'02/07/2023 05:20:37';LHCInfo;337;0.52;149;28.4564;7251086920971714560;02/07/2023 07:20:35;0.0;0.0;;;;;;;;;                                                            0.0;0.0;
# :Traceback (most recent call last):
#   File "/eos/home-j/jchyczyn/popcon-2023-pr/CMSSW_13_1_0_pre3/src/CondTools/RunInfo/python/ppsLHCInfoOldPerLSComp.py", line 147, in <module>
#     main()
#   File "/eos/home-j/jchyczyn/popcon-2023-pr/CMSSW_13_1_0_pre3/src/CondTools/RunInfo/python/ppsLHCInfoOldPerLSComp.py", line 97, in main
#     while(abs(pps_timestamp-int(split_lhc[2])) < 10*60 and split_pps[2] == split_lhc[3]):
# IndexError: list index out of range