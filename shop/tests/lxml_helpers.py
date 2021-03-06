import lxml.html


class ChangeListPage:
    """モデル一覧画面の画面項目検証用クラス"""

    def __init__(self, rendered_content):
        self.parsed_content = lxml.html.fromstring(rendered_content)

    @property
    def result_list(self):
        """検索結果テーブルのHTMLElementオブジェクト"""
        elements = self.parsed_content.xpath('//table[@id="result_list"]')
        return elements[0] if elements else None

    @property
    def result_list_header_texts(self):
        """検索結果テーブルのヘッダの表示内容"""
        if self.result_list is None:
            return None
        head = self.result_list.xpath('thead/tr')[0]
        return [e.text_content() for e in head.xpath('th[contains(@class, "column-")]/div[@class="text"]')]

    @property
    def result_list_rows_texts(self):
        """検索結果テーブルのデータ行の表示内容"""
        if self.result_list is None:
            return None
        rows = self.result_list.xpath('tbody/tr')
        return [[e.text_content() for e in row.xpath('td[contains(@class, "field-")]')] for row in rows]

    # @property
    # def result_count_text(self):
    #     """合計件数の表示内容"""
    #     elements = self.parsed_content.xpath(
    #         '//form[@id="changelist-form"]/p[@class="paginator"]/text()')
    #     elements = [e.strip() for e in elements if len(e.strip()) > 0]
    #     # ['<合計件数>'] or ['…', '<合計件数>'] となるので最後の要素を返す
    #     return elements[-1] if elements else None
    #
    # @property
    # def paginator_this_page_text(self):
    #     """ページネーションの現在ページの表示内容"""
    #     elements = self.parsed_content.xpath(
    #         '//form[@id="changelist-form"]/p[@class="paginator"]/span')
    #     return elements[0].text if elements else None
    #
    # @property
    # def paginator_link_texts(self):
    #     """ページネーションのページ移動リンクの表示内容"""
    #     elements = self.parsed_content.xpath(
    #         '//form[@id="changelist-form"]/p[@class="paginator"]/a')
    #     return [e.text for e in elements] if elements else None
    #
    # @property
    # def action_list_texts(self):
    #     """アクション一覧の選択肢の表示内容"""
    #     elements = self.parsed_content.xpath(
    #         '//form[@id="changelist-form"]/div[@class="actions"]//select/option')
    #     return [e.text for e in elements] if elements else None
    #
    # @property
    # def add_button(self):
    #     """追加ボタンのHTMLElementオブジェクト"""
    #     elements = self.parsed_content.xpath('//a[@class="addlink"]')
    #     return elements[0] if elements else None
    #
    # @property
    # def search_form(self):
    #     """簡易検索フォームのHTMLElementオブジェクト"""
    #     elements = self.parsed_content.xpath('//form[@id="changelist-search"]')
    #     return elements[0] if elements else None
    #
    # @property
    # def filter_headers(self):
    #     """絞り込み（フィルタ）のh3タイトルの表示内容"""
    #     elements = self.parsed_content.xpath('//div[@id="changelist-filter"]/h3')
    #     return [e.text for e in elements] if elements else None
    #
    # @property
    # def filter_choices_texts(self):
    #     """絞り込み（フィルタ）の選択肢の表示内容"""
    #     elements = self.parsed_content.xpath(
    #         '//div[@id="changelist-filter"]/ul')
    #     return [[
    #         choice.text_content().strip() for choice in e.findall('li')
    #     ] for e in elements] if elements else None
    #
    # @property
    # def success_message(self):
    #     """成功メッセージの表示内容"""
    #     elements = self.parsed_content.xpath(
    #         '//ul[@class="messagelist"]/li[@class="success"]')
    #     return elements[0].text_content() if elements else None
    #
    # @property
    # def warning_message(self):
    #     """警告メッセージの表示内容"""
    #     elements = self.parsed_content.xpath(
    #         '//ul[@class="messagelist"]/li[@class="warning"]')
    #     return elements[0].text_content() if elements else None
