# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcase\goods\add\add_goods_price.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcase.login.login_success_test import TestCaseLoginSuccess as LoginSuccess


class TestCaseAddGoodsPrice(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "goodsname-goodscode-price-code-msg": [
                    ["yoyo123", "${goods_code()}", None, 0, "success!"],
                    ["yoyo123", "${goods_code()}", 21, 0, "success!"],
                    ["yoyo123", "${goods_code()}", 21.99, 0, "success!"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("添加商品-成功")
        .variables(
            **{
                "goodsname": "yoyo",
                "goodscode": "${goods_code()}",
                "merchantid": "10001",
                "merchantname": "悠悠学堂",
                "goodsprice": 99.9,
                "stock": 100,
                "goodsgroupid": 0,
                "goodsstatus": 1,
                "price": 21.0,
            }
        )
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(RunTestCase("step1-login").call(LoginSuccess).export(*["token"])),
        Step(
            RunRequest("添加商品")
            .post("/api/v2/goods")
            .with_headers(**{"Authorization": "Token $token"})
            .with_json(
                {
                    "goodsname": "$goodsname",
                    "goodscode": "$goodscode",
                    "merchantid": "$merchantid",
                    "merchantname": "$merchantname",
                    "goodsprice": "$goodsprice",
                    "stock": "$stock",
                    "goodsgroupid": "$goodsgroupid",
                    "goodsstatus": "$goodsstatus",
                    "price": "$price",
                }
            )
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCaseAddGoodsPrice().test_start()
