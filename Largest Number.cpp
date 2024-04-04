class Solution {
public:
    static bool comp(const string& a,const string& b)
    {
        int al = a.length();
        int bl = b.length();

        for(int i{0};i < max(al,bl) * 2;i++)
        {
            if(a[i % al] != b[i % bl])
            {
                return a[i % al] > b[i % bl];
            }
        }
        return 0;
    }
    string largestNumber(vector<int>& nums) {
        
        vector<string> snums;

        for(int x : nums)
        snums.push_back(to_string(x));

        sort(snums.begin(),snums.end(),comp);

        string s;
        for(string t: snums)
        s += t;

        return (s[0] != '0')? s : "0";
    }
};
