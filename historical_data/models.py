from django.db import models
from customer.models import Customer


class Credit(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="credit",
        db_index=True,
    )
    date = models.IntegerField() 
    quarter = models.IntegerField() 
    credit_count = models.IntegerField()
    averageCreditAmount = models.BigIntegerField()
    maxCreditAmount = models.BigIntegerField()
    minCreditAmount = models.BigIntegerField()
    totalCreditAmount = models.BigIntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "credit"
        verbose_name_plural = "credits"
        db_table = "credit_historical"

class Option(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="option",
        db_index=True,
    )
    date = models.IntegerField() 
    quarter = models.IntegerField() 
    countOptiontrade = models.IntegerField()
    countOptionstock = models.IntegerField()
    totalOptiontradeAmount = models.BigIntegerField()
    averageOptiontradeAmount = models.BigIntegerField()
    maxOptiontradeAmount = models.BigIntegerField()
    minOptiontradeAmount = models.BigIntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "option"
        verbose_name_plural = "option"
        db_table = "option_historical"

class Trade(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="trade",
        db_index=True,
    )
    date = models.IntegerField(db_index=True) 
    quarter = models.IntegerField(db_index=True) 
    countTradeStock = models.IntegerField()
    countallTrade = models.IntegerField()
    countBuyTrade = models.IntegerField()
    countSellTrade = models.IntegerField()
    totalTradeAmount = models.BigIntegerField()
    totalBuyTradeAmount = models.BigIntegerField()
    totalSellTradeAmount = models.BigIntegerField()
    averageallTradeAmount = models.BigIntegerField()
    averageBuyTradeAmount = models.BigIntegerField()
    averageSellTradeAmount = models.BigIntegerField()
    maxTradeAmount = models.BigIntegerField()
    minTradeAmount = models.BigIntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "Trade"
        verbose_name_plural = "Trade"
        db_table = "trade_historical"

class Login(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="login",
        db_index=True,
    )
    date = models.IntegerField() 
    quarter = models.IntegerField() 
    countLogin = models.IntegerField()
    distinctLoginweekDayNo = models.IntegerField()
    distinctLoginmonthDayNo = models.IntegerField()
    modeLoginmonthDayNo = models.IntegerField()
    modeLoginweekDayNo = models.IntegerField()
    averageLoginfrequency = models.IntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "login"
        verbose_name_plural = "logins"
        db_table = "login_historical"

class CashFlow(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="cashflow",
        db_index=True,
    )
    date = models.IntegerField() 
    quarter = models.IntegerField() 
    totalDepositAmount = models.BigIntegerField()
    averageDepositAmount = models.BigIntegerField()
    totalWithdrawAmount = models.BigIntegerField()
    averageWithdrawAmount = models.BigIntegerField()
    maxCashFlowAmount = models.BigIntegerField()
    minCashFlowAmount = models.BigIntegerField()
    absoluteRevenue = models.BigIntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "cashflow"
        verbose_name_plural = "cashflowes"
        db_table = "cashflow_historical"

class CashPortfolio(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="CashPortfo",
        db_index=True,
    )
    date = models.IntegerField() 
    weightedaverageCashAmount = models.BigIntegerField()
    averageCashAmount = models.BigIntegerField()
    maxCashAmount = models.BigIntegerField()
    minCashAmount = models.BigIntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "CashPortfo"
        verbose_name_plural = "CashPortfo"
        db_table = "CashPortfo_historical"

class Hami(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="hami",
        db_index=True,
    )
    date = models.IntegerField() 
    weightedaverageHamiquantity = models.BigIntegerField()
    averageHamiquantity = models.BigIntegerField()
    maxHamiquantity = models.BigIntegerField()
    minHamiquantity = models.BigIntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "hami"
        verbose_name_plural = "hami"
        db_table = "hami_historical"

class PortfolioValue(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="portfoliovalue",
        db_index=True,
    )
    date = models.IntegerField() 
    quarter = models.IntegerField() 
    averagePortfolioValue = models.BigIntegerField()
    maxPortfolioValue = models.BigIntegerField()
    minPortfolioValue = models.BigIntegerField()

    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "portfoliovalue"
        verbose_name_plural = "portfoliovalues"
        db_table = "portfoliovalue_historical"

class Fund(models.Model):
    customerKey = models.ForeignKey(
        Customer,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="fund",
        db_index=True,
    )
    date = models.IntegerField(db_index=True) 
    quarter = models.IntegerField(db_index=True) 
    countFundEbtal = models.IntegerField()
    countFundSodur = models.IntegerField()
    totalFundEbtalTradeAmount = models.BigIntegerField()
    totalFundSodurTradeAmount = models.BigIntegerField()
    averageallFundTradeAmount = models.BigIntegerField()
    averageFundEbtalTradeAmount = models.BigIntegerField()
    averageFundSodurTradeAmount = models.BigIntegerField()
    maxFundTradeAmount = models.BigIntegerField()
    minFundTradeAmount = models.BigIntegerField()
    
    def __str__(self):
        return self.customerKey

    class Meta:
        verbose_name = "fund"
        verbose_name_plural = "funds"
        db_table = "fund_historical"
