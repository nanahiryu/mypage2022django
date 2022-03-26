from django.db import models


class SubWeapon(models.Model):
    name = models.CharField('名前', max_length=64)
    explanation = models.TextField('説明', blank=True)

    class Meta:
        verbose_name = 'サブウェポン'
        verbose_name_plural = 'サブウェポン一覧'

    def __str__(self):
        return self.name


class Special(models.Model):
    name = models.CharField('名前', max_length=64)
    explanation = models.TextField('説明', blank=True)

    class Meta:
        verbose_name = 'スペシャル'
        verbose_name_plural = 'スペシャル一覧'

    def __str__(self):
        return self.name


class Weapon_class(models.Model):
    name = models.CharField('名前', max_length=64)

    class Meta:
        verbose_name = 'ブキ種'
        verbose_name_plural = 'ブキ種一覧'

    def __str__(self):
        return self.name


class Weight(models.Model):
    name = models.CharField('名前', max_length=64)

    class Meta:
        verbose_name = '重量'
        verbose_name_plural = '重量'

    def __str__(self):
        return self.name


class Attack_class(models.Model):
    name = models.CharField('名前', max_length=64)

    class Meta:
        verbose_name = '攻撃方法'
        verbose_name_plural = '攻撃方法'

    def __str__(self):
        return self.name


class Main(models.Model):
    name = models.CharField('名前', max_length=64)
    weapon_class = models.ForeignKey(Weapon_class, on_delete=models.PROTECT)
    weight = models.ForeignKey(Weight, on_delete=models.PROTECT)
    explanation = models.TextField('説明', blank=True)
    attacks = models.ManyToManyField(
        Attack_class,
        through='Range',
        through_fields=('main', 'range_name'),
    )

    class Meta:
        verbose_name = 'メイン'
        verbose_name_plural = 'メイン一覧'

    def __str__(self):
        return self.name


class Range(models.Model):
    range_name = models.ForeignKey(Attack_class, on_delete=models.PROTECT)
    main = models.ForeignKey(Main, on_delete=models.PROTECT)
    range = models.DecimalField('射程', max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = '射程'
        verbose_name_plural = '射程'

    def __str__(self):
        return f"{self.main}-{self.range_name}"


class Weapon(models.Model):
    name = models.CharField('ブキ名', max_length=64)
    main = models.ForeignKey(Main, on_delete=models.PROTECT)
    sub = models.ForeignKey(SubWeapon, on_delete=models.PROTECT)
    special = models.ForeignKey(Special, on_delete=models.PROTECT)
    sp_point = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'ブキ'
        verbose_name_plural = 'ブキ'

    def __str__(self):
        return self.name
