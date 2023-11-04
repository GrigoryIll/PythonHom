class Calculator:
    def calculateDiscount(self, purchase_amount, discount):
        if not isinstance(purchase_amount, (int, float)) or purchase_amount <= 0:
            raise ArithmeticError("Недопустимые аргументы")
        if not isinstance(discount, (int, float)) or discount < 0:
            raise ArithmeticError("Недопустимые аргументы")
        amount_to_pay = purchase_amount - purchase_amount * discount/100
        return amount_to_pay
