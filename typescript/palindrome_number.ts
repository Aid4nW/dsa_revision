function isPalindrome(x: number): boolean {
    let str_x = String(x);
    let half;
    if (str_x.length % 2 == 0) {
        half = str_x.length / 2
        if (str_x.slice(half) == str_x.slice(0, half).split('').reverse().join('')) {
            return true
        }
        else {
            return false
        }
    }
    else {
        half = str_x.length / 2 >> 0
        if (str_x.slice(half + 1) == str_x.slice(0, half).split('').reverse().join('')) {
            return true
        }
        else {
            return false
        }
    }
};