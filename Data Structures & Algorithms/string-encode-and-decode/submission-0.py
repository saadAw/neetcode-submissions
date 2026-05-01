class Solution:
    def encode(self, strs: List[str]) -> str:

        encoded_strs = ""
        for strr in strs:
            str_length = f"{len(strr)}"
            encoded_strs += str_length.zfill(3) + strr
        return encoded_strs

    def decode(self, s: str) -> List[str]:

        strs = []

        while len(s)>0:
            length = int(s[:3])
            strs.append(s[3 : length + 3])
            s = s[length + 3:]

        return strs
