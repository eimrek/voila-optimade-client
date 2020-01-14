import ipywidgets as ipw


class StructureDataOutput(ipw.VBox):
    def __init__(self, data=None, **kwargs):
        """ Structure Data Output Widget
        Show structure data as a set of HTML widgets in a VBox widget.

        :param data: dict: Structure data with appropriate k,v-pairs
        """

        # Initiate
        self._data = {}.fromkeys(self._empty_values(), "")
        self._widget_data = self._empty_values()

        # Set hidden properties
        self._data = data
        self._set_widget_data(self._data)

        super(StructureDataOutput, self).__init__(
            children=self._get_widgets(), **kwargs
        )

    @property
    def data(self):
        # Set data if empty
        if self._data is None:
            self._data = self._empty_values()[:]["value"]
        # Getter
        return self._data

    @data.setter
    def data(self, value=None):
        """ Set data property
        It is assumed self._data ALWAYS is a dict with empty values
        and keys set from self._empty_values()
        """
        if value:
            # Check type
            if not isinstance(value, dict):
                raise TypeError("data must be a dict")

            # Check keys in dict are valid
            if self._valid_attributes(value):
                self._data.update(value)
                self._update_widget()
            else:
                raise ValueError(
                    "Non-valid structure attributes (data dict keys) "
                    "were provided. Valid attributes (keys) are: {}".format(
                        ",".join(list(self._empty_values().keys()))
                    )
                )

    def _valid_attributes(self, data):
        """ Check if keys in data are valid
        :param data: dict proposed to be updated in self._data
        :return: bool: True if keys in data are a subset of keys in _empty_values(),
                 False otherwise.
        """
        valid_keys = list(self._empty_values().keys())
        for key in data:
            if key not in valid_keys:
                return False
        return True

    def _set_values(self, data):
        """ Set structure data out values
        :param data: dict: Structure data
        """
        # Check
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        # Update values
        return data

    def _empty_values(self):
        """ Return dict 'schema' with empty values
        :return: dict: 'schema' of structure attributes with empty values
        """
        data_out = {
            "formula": {
                "widget": ipw.HTML(),
                "title": "<b>{}</b>: ".format("Chemical formula"),
                "value": "",
            },
            "elements": {
                "widget": ipw.HTML(),
                "title": "<b>{}</b>: ".format("Elements"),
                "value": "",
            },
            "nelements": {
                "widget": ipw.HTML(),
                "title": "<b>{}</b>: ".format("Number of elements"),
                "value": "",
            },
            "nsites": {
                "widget": ipw.HTML(),
                "title": "<b>{}</b>: ".format("Number of sites in unit cell"),
                "value": "",
            },
            "unitcell": {
                "widget": ipw.HTMLMath(),
                "title": "<b>{}</b>: ".format("Unit cell"),
                "value": "",
            },
        }
        return data_out

    def _set_widget_data(self, data):
        for structure_attribute, value in data.items():
            # Update "value"
            self._widget_data[structure_attribute]["value"] = value

    def _get_widgets(self):
        widgets = []
        for structure_attribute, widget_data in self._widget_data.items():
            if structure_attribute == "unitcell":
                value = self._unit_cell(widget_data["value"])
            else:
                value = str(widget_data["value"])

            widget = widget_data["widget"]
            widget.value = widget_data["title"] + value

            widgets.append(widget)
        return widgets

    def _update_widget(self):
        self._set_widget_data(self._data)
        self.children = self._get_widgets()

    def _unit_cell(self, uc):
        if isinstance(uc, list):
            out = r"$\Bigl(\begin{smallmatrix} "
            for i in range(len(uc[0]) - 1):
                row = list()
                for vector in uc:
                    row.append(vector[i])
                out += r" & ".join([str(x) for x in row])
                out += r" \\ "
            row = list()
            for vector in uc:
                row.append(vector[-1])
            out += r" & ".join([str(x) for x in row])
            out += r" \end{smallmatrix} \Bigr)$"
        elif isinstance(uc, str):
            out = uc
        else:
            raise TypeError("Value of unit cell must be given as a list (of lists)")

        return out
