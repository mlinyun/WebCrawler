# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsScraperPipeline:
    def process_item(self, item, spider):
        return item


# class DbWriterPipeline:
#     def open_spider(self, spider):
#         # 链接数据库，启动爬虫时调用此方法
#         self.db_manager = MySQL
#
#     def close_spider(self, spider):
#         # 关闭数据库，关闭爬虫时调用此方法
#         self.db_manager.close()
#
#     def process_item(self, item, spider):
#         # 将 item 的数据转为字符串，并插入数据库
#         import json
#         line = json.dumps(dict(item))
#         self.db_manager.insert(line)
#         return item
#
#     def laod_columns(self, table_name):
#         # 获得数据表的字段信息
#         sql = "SELECT column_name FROM information_schema.columns WHERE table_schema='{}' AND table_name='{}'".format(
#             self.db_name, table_name)
#         frecs = self.fetch_records(sql)
#         flds = list([t[0] for t in frecs])
#         return flds
#
#     def save_to_db(self, item):
#         valid_flds = list(
#             [fld for fld in self.flds if fld in item and item[fld]])
#         sql = "INSERT INTO {}.{}({}) VALUES({})".format(
#             self.db_name,
#             self.table_name,
#             ','.join(valid_flds),
#             ','.join(['%s'] * len(valid_flds))
#         )
#         vals = [tuple(item[fld] for fld in valid_flds)]
#         return self.dbm.insert_records(sql, vals)  # 正常插入成功
