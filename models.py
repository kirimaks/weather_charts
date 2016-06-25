def make_models(db):
    class Chart(db.Model):
        __tablename__ = "charts"
        chart_id = db.Column(db.Integer, primary_key=True)
        chart_name = db.Column(db.String(256), nullable=False)

        # Ref.
        data = db.relationship("Data", backref="Chart")

        def __repr__(self):
            return "[{}] {}".format(self.chart_id, self.chart_name)

    class Data(db.Model):
        __tablename__ = "data"
        ref_id = db.Column(db.Integer, primary_key=True)
        indicator = db.Column(db.Integer, nullable=False)
        chart_id = db.Column(db.Integer, db.ForeignKey("charts.chart_id"))

        def __repr__(self):
            pass
