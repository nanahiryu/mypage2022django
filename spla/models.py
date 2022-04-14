from django.db import models


class SubWeapon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('名前', max_length=64)
    explanation = models.TextField('説明', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="sub_img")

    class Meta:
        verbose_name = 'サブウェポン'
        verbose_name_plural = 'サブウェポン一覧'

    def __str__(self):
        return self.name


class Special(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('名前', max_length=64)
    explanation = models.TextField('説明', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="sp_img")

    class Meta:
        verbose_name = 'スペシャル'
        verbose_name_plural = 'スペシャル一覧'

    def __str__(self):
        return self.name


class Weapon_class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('名前', max_length=64)
    explanation = models.TextField('説明', blank=True)

    class Meta:
        verbose_name = 'ブキ種'
        verbose_name_plural = 'ブキ種一覧'

    def __str__(self):
        return self.name


class Weight(models.Model):
    id = models.IntegerField(primary_key=True)
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
    id = models.IntegerField(primary_key=True)
    name = models.CharField('名前', max_length=64)
    weapon_class = models.ForeignKey(Weapon_class, on_delete=models.PROTECT)
    weight = models.ForeignKey(Weight, on_delete=models.PROTECT)
    explanation = models.TextField('説明', blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="main_img")
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
    range_name = models.ForeignKey(
        Attack_class, on_delete=models.PROTECT, related_name='range')
    main = models.ForeignKey(
        Main, on_delete=models.PROTECT, related_name='range')
    range = models.DecimalField('射程', max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = '射程'
        verbose_name_plural = '射程'

    def __str__(self):
        return f"{self.main}-{self.range_name}"


class Weapon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('ブキ名', max_length=64)
    main = models.ForeignKey(
        Main, on_delete=models.PROTECT, related_name='weapon')
    sub = models.ForeignKey(
        SubWeapon, on_delete=models.PROTECT, related_name='weapon')
    special = models.ForeignKey(
        Special, on_delete=models.PROTECT, related_name='weapon')
    sp_point = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to="weapon_img")

    class Meta:
        verbose_name = 'ブキ'
        verbose_name_plural = 'ブキ一覧'

    def __str__(self):
        return self.name
