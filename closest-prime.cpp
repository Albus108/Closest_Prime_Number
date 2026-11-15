#include <iostream>

bool isPrime(int n){
        if(n<2){
            return false;
        }

        if(n==2){
            return true;
        }

        if(n%2==0){
            return false;
        }
    
        for(int i=3;i*i<=n;i=i+2){
            if(n%i==0){
                return false;
            }
        }

        return true;
}

int main(){

    int n;
    std::cout<<"Enter a number: ";
    std::cin>>n;  

    if(isPrime(n)){
        std::cout<<n<<" is prime\n";
    }

    else{
        std::cout<<n<<" is composite\n";

        int y,z;

        if(n%2==0){
            y=n+1;
            z=n-1;
        }
        else{
            y=n+2;
            z=n-2;
        }
            
        while(!isPrime(y)){
            y=y+2;
        }
        
        while(z>=2&&!isPrime(z)){
            z=z-2;
        }

        int a=std::abs(n-y);

        if(z<2){
            std::cout<<"\nClosest prime to "<<n<<" is "<<y;
        }
        else{

            int b=std::abs(n-z);

            if(a<b){
                std::cout<<"Closest prime number to "<<n<<" is "<<y;
            }
            else if(a==b){
                std::cout<<"Closest prime numbers to "<<n<<" are "<<y<<" and "<<z;
            }
            else{
                std::cout<<"Closest prime number to "<<n<<" is "<<z;
            }
        }
    }

    return 0;

}