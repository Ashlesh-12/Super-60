#include <stdio.h>



int main()

{

    int multiple = 61, d = 60*7, rest ;

    int count = 1;

    int iterations = 0;

    while(count<=10)

    {
           ++iterations;

        if (count == 1)

        {

            while(multiple % 7 != 0)

            {

                multiple += 60;

            }

            ++count;

            printf("%d\n", multiple);

        }



        if (count == 3)

        {

            ++count;

        }



        if(count != 3)

        {

            rest = multiple + ((count - 1)*d);

            printf("%d\n", rest);

            ++count;

        }

     

    }

    printf("%d\n", iterations);

    return 0;

}

//2 iterations

// credits: koshin

 