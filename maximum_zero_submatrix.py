# O(nm)
def maximum_zero_submatrix(n,m,a):
    ans=0
    d,d1,d2=m*[-1],m*[-1],m*[-1]
    st=[]
    for i in range(n):
        for j in range(m):
            if a[i][j]!=0:
                d[j]=i
        st=[]
        for k in range(m):
            while len(st)>0 and d[st[-1]]<=d[k]:
                st.pop()
            if len(st)>0:
                d1[k]=st[-1]
            else:
                d1[k]=-1
            st.append(k)
        st=[]
        for r in range(m-1,-1,-1):
            while len(st)>0 and d[st[-1]]<=d[r]:
                st.pop()
            if len(st)>0:
                d2[r]=st[-1]
            else:
                d2[r]=m
            st.append(r)
        for t in range(m):
            ans=max(ans,(i-d[t])*(d2[t]-d1[t]-1))
    return ans

n=6
m=6
a=[[1,2,3,4,5,1],
   [1,0,0,0,4,1],
   [1,0,0,0,5,1],
   [1,0,0,0,6,1],
   [1,0,9,8,7,1],
   [1,8,1,7,1,1]]

assert maximum_zero_submatrix(n,m,a) == 9
