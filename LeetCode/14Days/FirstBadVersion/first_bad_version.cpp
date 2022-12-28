// The API isBadVersion is defined for you.
bool isBadVersion(int version);
class Solution
{
public:
    int firstBadVersion(long n)
    {
        long z(0);
        while (z != n)
        {
            long m(((n + z) % 2) ? (n + z) / 2 + 1 : (n + z) / 2);
            if (isBadVersion(m))
            {
                n = m - 1;
            }
            else
            {
                z = m;
            }
        }
        return int(z + 1);
    }
};