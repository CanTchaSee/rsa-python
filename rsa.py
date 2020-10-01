class RSA:
    def is_prime(self,n):
        if n == 1 or n == 2:
            return True
        if not(n%2) or not(n%5):
            return False
        else:
            p = 2
            while p**2 <= n:
                if not(n%p):
                    return False
                p += 2
            return True
    def soe(self,n):
        final = []
        P = [True for i in range(n+1)]
        p = 2
        while p**2 <= n:
            if P[p]:
                for i in range(p*2, n+1, p):
                    P[i] = False
            p += 1
        P[0] = False
        P[1] = False
        for p in range(n+1):
            if P[p]:
                final.append(p)
        return final
    def gen_two_prime(self,n):
        i = (5**n)
        p = self.soe(i)
        q = p[-1]
        p = p[int(len(p)/2)]
        return p,q
    def gcd(self,p,q):
        while (q>0):
            r = p%q
            p,q = q,r
        return p
    def egcd(self,a,b):
        o_r,r = a,b
        o_s,s = 1,0
        o_t,t = 0,1
        while r:
            q = o_r//r
            o_r,r = r,o_r-q*r
            o_s,s = s,o_s-q*s
            o_t,t = t,o_t-q*t
        return o_s,o_t
    def pegcd(self,a,b):
        s,t=self.egcd(a,b)
        k = 0
        r = lambda k: s+k*b
        i = r(k)
        while i<0:
            k += 1
            i = r(k)
        return i
    def get_e(self,l):
        P = self.soe(l)
        e = []
        q = len(P)-1
        while q > 0:
            if self.gcd(P[q],l) == 1:
                return P[q]
            q -= 1
    def get_keys(self,p,q):
        if not(self.is_prime(p) and self.is_prime(q)):
            print("p & q must be primes")
            exit()
        n,l = p*q,(p-1)*(q-1)
        e = self.get_e(l)
        d = self.pegcd(e,l)
        return [(n,e),(n,d)]
    def crypt(self,t,key):
        return (t**key[1])%key[0]
    def block(self,n,m):
        a = len(hex(n)[2:])
        x = hex(m)[2:]
        q = a - len(x)
        return '0'*q+x
    def encrypt(self,m,key):
        r = ''
        for char in m:
            r += self.block(key[0],self.crypt(ord(char),key))
        return r
    def decrypt(self,c,key):
        r = ''
        q = len(hex(key[0])[2:])
        p = 0
        while p < len(c):
            r += chr(self.crypt(int(c[p:p+q],16),key))
            p += q
        return r
