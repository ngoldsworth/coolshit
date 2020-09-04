/**
 * GRANT GOLDSWORTH - 1164709
 * QUIZ 2 - PROGRAMMING
 * CS 4A #16845
 * LAST MODIFIED 20:45 9/3/2020
 * ----------------------------------------
 * This program will prompt the user for input, and calculate
 * a mortgage based on the information. User inputs:
 *  - a loan amount
 *  - annual interest rate as percent
 *  - loan term in years
 */

import java.util.Scanner;

 public class MortgageCalculator {
     public static void main(String[] args) {
        
        int     loanAmount          = 0;
        double  annualInterestRate  = 0;
        double  monthlyInterestRate = 0;
        int     loanTerm            = 0;
        double  monthlyPayment      = 0;
        double  totalAmountPaid     = 0;
        double  totalInterestPaid   = 0;
        boolean isInvalidInput      = false;

        Scanner input = new Scanner(System.in);




        // obtain input that acts as main while loop's control variable
        // ensure the input is acceptable as well - loop until valid input is obtained
        do {
            System.out.print("Please enter a positive integer for the loan amount: ");
            loanAmount = input.nextInt();

            // output the additional error message for invalid input
            isInvalidInput = (loanAmount < 0);
            if (isInvalidInput) {
                System.out.print("RETRY: ");
            }
        } while (isInvalidInput);



        // continue to loop while the loanAmount is not 0, continuously prompting
        // user to input data for new sets of calculations
        while(loanAmount != 0) {


            /* INPUT STATEMENTS - Gather and error check input from user */

            // obtain acceptable input for interest rate
            do {
                System.out.print("Please enter a positive number for the annual interest rate: ");
                annualInterestRate = input.nextDouble();

                // output the additional error message for invalid input
                isInvalidInput = (annualInterestRate <= 0);
                if (isInvalidInput) {
                    System.out.print("RETRY: ");
                }
            } while (isInvalidInput);


            // obtain acceptable input for loan term
            do {
                System.out.print("Please enter a positive integer for the term in years: ");
                loanTerm = input.nextInt();

                // output the additional error message for invalid input
                isInvalidInput = (loanTerm <= 0);
                if (isInvalidInput) {
                    System.out.print("RETRY: ");
                }
            } while (isInvalidInput);

            /* PROCESSING */
            // crunch the numbers and get that principle
            // calculate the monthly interest rate and convert from percent to decimal
            // ensure that loanTerm is in months
            monthlyInterestRate = annualInterestRate / 12 / 100;
            monthlyPayment = (loanAmount * (monthlyInterestRate * Math.pow((1 + monthlyInterestRate), loanTerm * 12))) 
                             / (Math.pow((1 + monthlyInterestRate), loanTerm * 12) - 1);

            // calculate the total amount paid and total interest paid
            totalAmountPaid = monthlyPayment * 12 * loanTerm;
            totalInterestPaid = totalAmountPaid - loanAmount;


            /* OUTPUT - Output the data in a table with specific formats for different data representations */
            // output the formatted data table
            System.out.print("\nFor a loan with these characteristics:\n");
            System.out.printf("      $%8d\n", loanAmount);
            System.out.printf("      %4.2f annual interest rate\n", annualInterestRate);
            System.out.printf("%8d year term\n\n", loanTerm);

            System.out.printf("The Monthly Payment = $%8.2f\n", monthlyPayment);
            System.out.printf("The Total Amount Paid = $%8.2f\n", totalAmountPaid);
            System.out.printf("The Total Interest Paid = $%8.2f\n", totalInterestPaid);

            System.out.print("\n\n");


            // start of next round of calculations
            // obtain acceptable input for loan amount - UPDATING THE LOOP CONTROL VAR
            do {
                System.out.print("Please enter a positive integer for the loan amount: ");
                loanAmount = input.nextInt();

                // output the additional error message for invalid input
                isInvalidInput = (loanAmount < 0);
                if (isInvalidInput) {
                    System.out.print("RETRY: ");
                }
            } while (isInvalidInput);
        }

        System.out.print("THANK YOU FOR USING THE MORTGAGE CALCULATOR!!");
     }
 }