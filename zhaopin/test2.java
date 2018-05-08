package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class Test2 {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "http://192.168.10.202/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void test2() throws Exception {
    driver.get(baseUrl + "/view/main.html");
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("15728042309");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("贷前管理")).click();
    driver.findElement(By.linkText("资信管理")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_26 | ]]
    driver.findElement(By.id("launchedCredit")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    // ERROR: Caught exception [unknown command [storeZhong]]
    // ERROR: Caught exception [unknown command [storeName]]
    // ERROR: Caught exception [unknown command [storeMobie]]
    // ERROR: Caught exception [unknown command [storeShenfen]]
    driver.findElement(By.name("customerName")).clear();
    driver.findElement(By.name("customerName")).sendKeys("${name}");
    driver.findElement(By.name("relavants[0].fullName")).clear();
    driver.findElement(By.name("relavants[0].fullName")).sendKeys("${name}");
    new Select(driver.findElement(By.id("cardType"))).selectByVisibleText("身份证");
    // ERROR: Caught exception [unknown command [storeRandom]]
    driver.findElement(By.id("cardNo")).clear();
    driver.findElement(By.id("cardNo")).sendKeys("${shenfen}");
    driver.findElement(By.name("relavants[0].cardId")).clear();
    driver.findElement(By.name("relavants[0].cardId")).sendKeys("${shenfen}");
    driver.findElement(By.name("estimateLoanAmount")).clear();
    driver.findElement(By.name("estimateLoanAmount")).sendKeys("100000");
    new Select(driver.findElement(By.id("bankDeraler"))).selectByVisibleText("工行安徽城建支行");
    new Select(driver.findElement(By.id("maritalStatus"))).selectByVisibleText("未婚");
    driver.findElement(By.name("relavants[0].mobile")).clear();
    driver.findElement(By.name("relavants[0].mobile")).sendKeys("${mobie}");
    driver.findElement(By.cssSelector("input.hide")).clear();
    driver.findElement(By.cssSelector("input.hide")).sendKeys("C:\\Users\\mxj\\Desktop\\错误捕捉1\\timg：1.jpg");
    driver.findElement(By.cssSelector("input.hide")).clear();
    driver.findElement(By.cssSelector("input.hide")).sendKeys("C:\\Users\\mxj\\Desktop\\错误捕捉1\\3205221987120680271[1].jpg");
    driver.findElement(By.cssSelector("input.hide")).clear();
    driver.findElement(By.cssSelector("input.hide")).sendKeys("C:\\Users\\mxj\\Desktop\\错误捕捉1\\151029110134718[1].jpg");
    // ERROR: Caught exception [unknown command [storeName]]
    // ERROR: Caught exception [unknown command [storeMobie]]
    // ERROR: Caught exception [unknown command [storeShenfen]]
    driver.findElement(By.id("addParty")).click();
    driver.findElement(By.name("relavants[1].fullName")).clear();
    driver.findElement(By.name("relavants[1].fullName")).sendKeys("${name}");
    new Select(driver.findElement(By.id("cardType"))).selectByVisibleText("身份证");
    // ERROR: Caught exception [unknown command [storeRandom]]
    driver.findElement(By.name("relavants[1].cardId")).clear();
    driver.findElement(By.name("relavants[1].cardId")).sendKeys("${shenfen}");
    driver.findElement(By.name("estimateLoanAmount")).clear();
    driver.findElement(By.name("estimateLoanAmount")).sendKeys("30000");
    new Select(driver.findElement(By.id("bankDeraler"))).selectByVisibleText("工行安徽城建支行");
    driver.findElement(By.name("relavants[1].mobile")).clear();
    driver.findElement(By.name("relavants[1].mobile")).sendKeys("${mobie}");
    new Select(driver.findElement(By.name("relavants[1].borrowerRelationship"))).selectByVisibleText("父亲");
    new Select(driver.findElement(By.name("relavants[1].guaranteeRelationship"))).selectByVisibleText("反担保人");
    driver.findElement(By.id("save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.cssSelector("#task > div.modal-dialog.modal-lg > div.modal-content > div.modal-header > button.close")).click();
    driver.findElement(By.id("save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(.//*[@id='table_3']/tbody/tr[4]/td[1]/input)")).click();
    driver.findElement(By.xpath("(//button[@type='button'])[21]")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("15129209059");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("征信流程");
    driver.findElement(By.cssSelector("option[value=\"CREDIT_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("征信录入")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    new Select(driver.findElement(By.name("relavants[0].checkResult"))).selectByVisibleText("通过");
    driver.findElement(By.xpath("(.//*[@id='partyBox']/div/div[2]/div[3]/div[2]/fieldset/div[1]/div[3]/div/input)")).click();
    driver.findElement(By.xpath("(html/body/div[8]/div[3]/table/tfoot/tr/th)")).click();
    // ERROR: Caught exception [Error: unknown strategy [class] for locator [class=today]]
    new Select(driver.findElement(By.name("relavants[1].checkResult"))).selectByVisibleText("通过");
    driver.findElement(By.xpath("(//input[@name='relavants[0].loanRepayment'])[2]")).click();
    driver.findElement(By.xpath("(//input[@name='relavants[1].loanRepayment'])[2]")).click();
    driver.findElement(By.id("save")).click();
    driver.findElement(By.id("sureOption")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("15728042309");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.xpath("//a[contains(text(),'我的任务')]")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("征信流程");
    driver.findElement(By.cssSelector("option[value=\"CREDIT_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("征信接受")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_undefined | ]]
    driver.findElement(By.id("save")).click();
    driver.findElement(By.id("sureOption")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.linkText("贷前管理")).click();
    driver.findElement(By.linkText("贷款评审")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_27 | ]]
    driver.findElement(By.xpath("(//button[@type='button'])[3]")).click();
    driver.findElement(By.id("sure")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    new Select(driver.findElement(By.id("product"))).selectByVisibleText("信用卡贷款(普通模式)");
    new Select(driver.findElement(By.id("product"))).selectByVisibleText("银行直销-非垫款");
    new Select(driver.findElement(By.id("product"))).selectByVisibleText("工行@车贷");
    new Select(driver.findElement(By.id("productId"))).selectByVisibleText("众泰39980元购");
    driver.findElement(By.id("isDiscount2")).click();
    driver.findElement(By.xpath("//div[@id='isSupportDiscount_se']/div/label[2]")).click();
    driver.findElement(By.xpath("(//input[@name='isDidi'])[2]")).click();
    new Select(driver.findElement(By.id("carProvince"))).selectByVisibleText("浙江省");
    new Select(driver.findElement(By.id("carCity"))).selectByVisibleText("湖州市");
    driver.findElement(By.id("getBrand")).click();
    driver.findElement(By.xpath("//div[@id='normal_cars']/div/div/ul/div/li[4]")).click();
    driver.findElement(By.id("getCarList")).click();
    driver.findElement(By.cssSelector("p")).click();
    driver.findElement(By.xpath("//div[@id='normal_cars']/div[2]/div/ul/li/ul/li[2]")).click();
    driver.findElement(By.id("getCarModel")).click();
    driver.findElement(By.xpath("//div[@id='normal_cars']/div[3]/div/ul/li/p")).click();
    driver.findElement(By.xpath("//div[@id='normal_cars']/div[3]/div/ul/li/ul/li")).click();
    driver.findElement(By.cssSelector("label.radio-inline > input[name=\"isTwoCard\"]")).click();
    driver.findElement(By.xpath("(//input[@name='isImported'])[2]")).click();
    new Select(driver.findElement(By.id("carDealer"))).selectByVisibleText("鄞州菲利普进口车");
    driver.findElement(By.id("billingPrice")).clear();
    driver.findElement(By.id("billingPrice")).sendKeys("120000");
    driver.findElement(By.name("billingPrice")).clear();
    driver.findElement(By.name("billingPrice")).sendKeys("120000");
    driver.findElement(By.id("loanAmount")).clear();
    driver.findElement(By.id("loanAmount")).sendKeys("76000");
    driver.findElement(By.id("carLoanAmount")).clear();
    driver.findElement(By.id("carLoanAmount")).sendKeys("60000");
    driver.findElement(By.id("purchaseTax")).clear();
    driver.findElement(By.id("purchaseTax")).sendKeys("8000");
    driver.findElement(By.id("insuranceAmount")).clear();
    driver.findElement(By.id("insuranceAmount")).sendKeys("6000");
    driver.findElement(By.id("decorateAmount")).clear();
    driver.findElement(By.id("decorateAmount")).sendKeys("2000");
    driver.findElement(By.id("consumeLoanAmount")).clear();
    driver.findElement(By.id("consumeLoanAmount")).sendKeys("16000");
    driver.findElement(By.name("repaymentAmount")).clear();
    driver.findElement(By.name("repaymentAmount")).sendKeys("2584.00");
    new Select(driver.findElement(By.id("province"))).selectByVisibleText("内蒙古自治区");
    driver.findElement(By.cssSelector("#province > option[value=\"150000\"]")).click();
    new Select(driver.findElement(By.id("city"))).selectByVisibleText("包头市");
    new Select(driver.findElement(By.id("area"))).selectByVisibleText("昆都仑区");
    driver.findElement(By.id("address")).clear();
    driver.findElement(By.id("address")).sendKeys("内蒙自治区");
    driver.findElement(By.cssSelector("div.BMap_contextMenu > div > span")).click();
    driver.findElement(By.name("visitAddressItude")).clear();
    driver.findElement(By.name("visitAddressItude")).sendKeys("120.467441 , 30.376231");
    driver.findElement(By.name("freeDoor")).clear();
    driver.findElement(By.name("freeDoor")).sendKeys("2");
    driver.findElement(By.id("preservation")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.linkText("客户评分卡A")).click();
    new Select(driver.findElement(By.xpath("(//select[@name='driverLicence'])[2]"))).selectByVisibleText("父母/子女有驾照");
    new Select(driver.findElement(By.xpath("(//select[@name='education'])[2]"))).selectByVisibleText("大专");
    new Select(driver.findElement(By.xpath("(//select[@id='housingStatus'])[2]"))).selectByVisibleText("父母住房");
    new Select(driver.findElement(By.id("profession_Code"))).selectByVisibleText("公务员");
    new Select(driver.findElement(By.xpath("(//select[@name='reservedFundsYear'])[3]"))).selectByVisibleText("无");
    new Select(driver.findElement(By.xpath("(//select[@name='industry'])[2]"))).selectByVisibleText("房地产行业");
    new Select(driver.findElement(By.xpath("(//select[@name='socialYear'])[3]"))).selectByVisibleText("1年以内");
    driver.findElement(By.id("btn_saveScoreCard")).click();
    driver.findElement(By.linkText("影像管理")).click();
    driver.findElement(By.id("tree_6_span")).click();
    driver.findElement(By.linkText("上传文件")).click();
    driver.findElement(By.id("upImageInput")).clear();
    driver.findElement(By.id("upImageInput")).sendKeys("C:\\Users\\mxj\\Desktop\\错误捕捉1\\151029110134718[1].jpg");
    driver.findElement(By.id("upload")).click();
    driver.findElement(By.linkText("预算单")).click();
    driver.findElement(By.xpath("(//*[@id='budget']/div/div/div/div/div/div[2]/button)")).click();
    driver.findElement(By.xpath("(//button[@type='button'])[14]")).click();
    driver.findElement(By.linkText("贷款信息")).click();
    driver.findElement(By.id("submit")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.cssSelector("button.btn.btn-default")).click();
    driver.findElement(By.cssSelector("label.radio-inline > input[name=\"positionMerge\"]")).click();
    driver.findElement(By.id("submit")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@username='曹晶晶'])")).click();
    driver.findElement(By.xpath("(//button[@type='button'])[34]")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.linkText("文档传递管理")).click();
    driver.findElement(By.linkText("文档传递")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_33 | ]]
    driver.findElement(By.xpath("(//button[@type='button'])[3]")).click();
    driver.findElement(By.linkText("发起文档传递")).click();
    driver.findElement(By.cssSelector("span.badge")).click();
    driver.findElement(By.id("sub")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='37'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("18710684534");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.cssSelector("option[value=\"LOAN_APPLY_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("中级审核（两证）")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.linkText("影像管理")).click();
    driver.findElement(By.id("tree_6_span")).click();
    driver.findElement(By.cssSelector("img[alt=\"151029110134718[1].jpg\"]")).click();
    driver.findElement(By.cssSelector("div.viewer-button.viewer-close")).click();
    driver.findElement(By.linkText("审批信息")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='153'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("15757829846");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.cssSelector("span.nav-label")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.cssSelector("option[value=\"LOAN_APPLY_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("付款申请")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.id("accountSelect2")).click();
    driver.findElement(By.linkText("选择")).click();
    driver.findElement(By.id("add")).click();
    driver.findElement(By.id("consumeLoan")).click();
    driver.findElement(By.cssSelector("#table_pay4 > tbody > tr > td > a.pay")).click();
    driver.findElement(By.name("isPayPurchaseTax")).click();
    driver.findElement(By.name("isPayInsuranceAmount")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='161'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("17306519184");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.cssSelector("option[value=\"LOAN_APPLY_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("付款审批")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='162'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("15990276159");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.cssSelector("option[value=\"LOAN_APPLY_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("资金划拨")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='163'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("13858258496");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.cssSelector("option[value=\"LOAN_APPLY_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("分公司付款")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.name("dealerPaymentRemark")).clear();
    driver.findElement(By.name("dealerPaymentRemark")).sendKeys("12345,上山打老虎");
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='30'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("13991814662");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.xpath("//a[contains(text(),'我的任务')]")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("业务录入")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.id("btn-baseInfo-save")).click();
    driver.findElement(By.name("cardNoValid")).click();
    driver.findElement(By.name("licenceIssuingAuthority")).clear();
    driver.findElement(By.name("licenceIssuingAuthority")).sendKeys("海曙公安局");
    driver.findElement(By.name("homePhone")).clear();
    driver.findElement(By.name("homePhone")).sendKeys("4112302");
    new Select(driver.findElement(By.id("post"))).selectByVisibleText("其他");
    driver.findElement(By.cssSelector("#post > option[value=\"5\"]")).click();
    new Select(driver.findElement(By.id("workNatureCode"))).selectByVisibleText("其他");
    driver.findElement(By.cssSelector("#workNatureCode > option[value=\"8\"]")).click();
    new Select(driver.findElement(By.name("domicileType"))).selectByVisibleText("农业");
    driver.findElement(By.cssSelector("select[name=\"domicileType\"] > option[value=\"1\"]")).click();
    new Select(driver.findElement(By.name("monthlyIncome"))).selectByVisibleText("10000-14999");
    driver.findElement(By.cssSelector("select[name=\"monthlyIncome\"] > option[value=\"3\"]")).click();
    driver.findElement(By.name("yearlyIncome")).clear();
    driver.findElement(By.name("yearlyIncome")).sendKeys("50");
    new Select(driver.findElement(By.name("reservedFunds"))).selectByVisibleText("1-500");
    driver.findElement(By.cssSelector("select[name=\"reservedFunds\"] > option[value=\"2\"]")).click();
    driver.findElement(By.name("cmpyPostcode")).clear();
    driver.findElement(By.name("cmpyPostcode")).sendKeys("421312");
    driver.findElement(By.name("homePostcode")).clear();
    driver.findElement(By.name("homePostcode")).sendKeys("41231");
    driver.findElement(By.name("companyName")).clear();
    driver.findElement(By.name("companyName")).sendKeys("渣男资产");
    driver.findElement(By.name("companyPhone")).clear();
    driver.findElement(By.name("companyPhone")).sendKeys("4118563");
    driver.findElement(By.name("employTime")).clear();
    driver.findElement(By.name("employTime")).sendKeys("2016-10-12");
    new Select(driver.findElement(By.id("province_2"))).selectByVisibleText("吉林省");
    driver.findElement(By.cssSelector("option[value=\"220000\"]")).click();
    new Select(driver.findElement(By.id("city_2"))).selectByVisibleText("通化市");
    driver.findElement(By.cssSelector("option[value=\"220500\"]")).click();
    new Select(driver.findElement(By.id("area_2"))).selectByVisibleText("通化县");
    driver.findElement(By.cssSelector("option[value=\"220521\"]")).click();
    driver.findElement(By.name("companyAddressDetail")).clear();
    driver.findElement(By.name("companyAddressDetail")).sendKeys("童话中你爱的");
    new Select(driver.findElement(By.id("province_1"))).selectByVisibleText("福建省");
    driver.findElement(By.cssSelector("#province_1 > option[value=\"350000\"]")).click();
    new Select(driver.findElement(By.id("city_1"))).selectByVisibleText("南平市");
    driver.findElement(By.cssSelector("option[value=\"350700\"]")).click();
    new Select(driver.findElement(By.id("area_1"))).selectByVisibleText("顺昌县");
    driver.findElement(By.cssSelector("option[value=\"350721\"]")).click();
    driver.findElement(By.name("homeAddressDetail")).clear();
    driver.findElement(By.name("homeAddressDetail")).sendKeys("我们胡建的");
    driver.findElement(By.name("curAddressTime")).clear();
    driver.findElement(By.name("curAddressTime")).sendKeys("2016-08-10");
    driver.findElement(By.id("btn-baseInfo-save")).click();
    driver.findElement(By.linkText("新增联系人")).click();
    driver.findElement(By.name("emergencyContact")).clear();
    driver.findElement(By.name("emergencyContact")).sendKeys("挂靠费");
    new Select(driver.findElement(By.name("relationship"))).selectByVisibleText("母亲");
    driver.findElement(By.xpath("(//input[@name='mobilePhone'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='mobilePhone'])[2]")).sendKeys("13506321630");
    driver.findElement(By.id("btn-contacter-save")).click();
    driver.findElement(By.linkText("新增联系人")).click();
    driver.findElement(By.name("emergencyContact")).clear();
    driver.findElement(By.name("emergencyContact")).sendKeys("儿童");
    new Select(driver.findElement(By.name("relationship"))).selectByVisibleText("兄弟");
    driver.findElement(By.xpath("(//input[@name='mobilePhone'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='mobilePhone'])[2]")).sendKeys("15785632203");
    driver.findElement(By.id("btn-contacter-save")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.linkText("反担保信息")).click();
    new Select(driver.findElement(By.xpath("(//select[@name='sex'])[2]"))).selectByVisibleText("男");
    driver.findElement(By.xpath("(//input[@name='birthday'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='birthday'])[2]")).sendKeys("1960-05-01");
    driver.findElement(By.xpath("(//input[@name='age'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='age'])[2]")).sendKeys("56");
    new Select(driver.findElement(By.xpath("(//select[@name='maritalStatus'])[2]"))).selectByVisibleText("已婚");
    new Select(driver.findElement(By.xpath("(//select[@name='education'])[2]"))).selectByVisibleText("高中");
    new Select(driver.findElement(By.xpath("(//select[@name='housingStatus'])[2]"))).selectByVisibleText("自建房");
    new Select(driver.findElement(By.cssSelector("select[name=\"professionCode\"]"))).selectByVisibleText("工人");
    new Select(driver.findElement(By.xpath("(//select[@name='industry'])[2]"))).selectByVisibleText("交通运输行业");
    new Select(driver.findElement(By.xpath("(//select[@name='monthlyIncome'])[2]"))).selectByVisibleText("5000-9999");
    driver.findElement(By.xpath("(//input[@name='companyName'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='companyName'])[2]")).sendKeys("老宁波牛杂面");
    driver.findElement(By.xpath("(//input[@name='companyPhone'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='companyPhone'])[2]")).sendKeys("4365856");
    new Select(driver.findElement(By.xpath("(//select[@name='reservedFunds'])[2]"))).selectByVisibleText("1-500");
    new Select(driver.findElement(By.xpath("(//select[@name='reservedFundsYear'])[2]"))).selectByVisibleText("1年以内");
    new Select(driver.findElement(By.xpath("(//select[@name='socialYear'])[2]"))).selectByVisibleText("1年以内");
    new Select(driver.findElement(By.id("provinceCode_0"))).selectByVisibleText("河北省");
    new Select(driver.findElement(By.id("cityCode_0"))).selectByVisibleText("秦皇岛市");
    new Select(driver.findElement(By.id("areaCode_0"))).selectByVisibleText("山海关区");
    driver.findElement(By.xpath("(//input[@name='companyAddressDetail'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='companyAddressDetail'])[2]")).sendKeys("福倍棱");
    new Select(driver.findElement(By.id("provinceCode_1_0"))).selectByVisibleText("河南省");
    new Select(driver.findElement(By.id("cityCode_1_0"))).selectByVisibleText("新乡市");
    new Select(driver.findElement(By.id("areaCode_1_0"))).selectByVisibleText("牧野区");
    driver.findElement(By.xpath("(//button[@type='button'])[12]")).click();
    driver.findElement(By.xpath("(//input[@name='homePhone'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='homePhone'])[2]")).sendKeys("4115260");
    driver.findElement(By.xpath("(//input[@name='homeAddressDetail'])[2]")).clear();
    driver.findElement(By.xpath("(//input[@name='homeAddressDetail'])[2]")).sendKeys("快点发过来");
    driver.findElement(By.xpath("(//*[@id='getLoanGuarantorInfo']/form/fieldset/div/div[2]/div/div[2]/button[1])")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='30'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("初级审核")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.linkText("影像管理")).click();
    driver.findElement(By.id("tree_6_span")).click();
    driver.findElement(By.cssSelector("img[alt=\"151029110134718[1].jpg\"]")).click();
    driver.findElement(By.cssSelector("div.viewer-button.viewer-close")).click();
    driver.findElement(By.linkText("审批信息")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.xpath("(//input[@value='81'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("18710684534");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.cssSelector("span.nav-label")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.cssSelector("option[value=\"LOAN_APPLY_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("中级审核")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.linkText("影像管理")).click();
    driver.findElement(By.id("tree_6_span")).click();
    driver.findElement(By.cssSelector("img[alt=\"151029110134718[1].jpg\"]")).click();
    driver.findElement(By.cssSelector("div.viewer-button.viewer-close")).click();
    driver.findElement(By.linkText("审批信息")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.xpath("(//input[@value='156'])")).click();
    driver.findElement(By.id("select-sign-btn")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.xpath("(//a[contains(text(),'我的任务')])[2]")).click();
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("18710684534");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    driver.findElement(By.linkText("中级审核")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
    driver.findElement(By.cssSelector("span.J_tabExit")).click();
    driver.findElement(By.id("exitSure")).click();
    driver.findElement(By.name("userName")).clear();
    driver.findElement(By.name("userName")).sendKeys("18606599629");
    driver.findElement(By.name("password")).clear();
    driver.findElement(By.name("password")).sendKeys("mao123456");
    driver.findElement(By.id("loginBtn")).click();
    driver.findElement(By.linkText("我的任务")).click();
    driver.findElement(By.cssSelector("li > a.J_menuItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectFrame | iframe_21 | ]]
    new Select(driver.findElement(By.id("ftCode"))).selectByVisibleText("贷款申请流程");
    driver.findElement(By.cssSelector("option[value=\"LOAN_APPLY_FLOW\"]")).click();
    driver.findElement(By.id("btn-search")).click();
    driver.findElement(By.linkText("总部审批中心")).click();
    driver.findElement(By.name("btSelectItem")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=iframe_undefined | ]]
    driver.findElement(By.xpath("(//input[@name='isConcernedCustomer'])[2]")).click();
    driver.findElement(By.xpath("(//input[@name='isAgency'])[2]")).click();
    driver.findElement(By.linkText("客户评分卡B")).click();
    driver.findElement(By.id("saveScore")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
    driver.findElement(By.linkText("影像管理")).click();
    driver.findElement(By.id("tree_6_span")).click();
    driver.findElement(By.cssSelector("img[alt=\"151029110134718[1].jpg\"]")).click();
    driver.findElement(By.cssSelector("div.viewer-button.viewer-close")).click();
    driver.findElement(By.id("btn-opinion-save")).click();
    driver.findElement(By.id("sureOption")).click();
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
