#!/usr/bin/env python3

m = int(input())
m_str = input()
n = int(input())
n_str = input()
m_lis = m_str.split()
m_num = list(map(int, m_lis))
n_lis = n_str.split()
n_num = list(map(int, n_lis))
n_st = set(n_num)
m_st = set(m_num)
dif_st = n_st.difference(m_st)
dif_st.update(m_st.difference(n_st))
dif_ls = list(dif_st)
dif_ls.sort()
for i in dif_ls:
    print(i)
