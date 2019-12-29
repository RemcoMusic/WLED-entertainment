import QtQuick 2.0
import QtQuick.Window 2.1
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.3
import QtQuick.Controls 1.0
import QtQuick.Controls.Universal 2.0

Window {
    id: devices_window
    title: "WLED-Entertainment - Devices"
    visible: true
    width: 480
    height: 480
    color: "#cfcdd7"

    GridLayout {
        id: gridLayout
        rowSpacing: 0
        columnSpacing: 0
        rows: 2
        columns: 1
        anchors.fill: parent

        RowLayout {
            id: rowLayout
            y: 0
            spacing: 0
            Layout.fillWidth: true
            Layout.minimumWidth: 480
            Layout.preferredWidth: 480
            Layout.preferredHeight: 240
            Layout.row: 1

            ListModel {
                id: wledListModel
                ListElement {
                    name: "New WLED Devices:    x.x.x.x"; checked:false
                }

                Component.onCompleted: {
                    dataToUI.getWled()
                }
            }

            ListView {
                Layout.fillWidth: true
                Layout.minimumWidth: 240
                Layout.preferredWidth: 240
                Layout.preferredHeight: 240
                model: wledListModel
                delegate: Text {
                    id: txt
                    text: name

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                                wledListModel.setProperty(index, "checked", !checked)
                            }
                    }

                    states: State {
                        name: "checked"
                        when: checked
                        PropertyChanges {
                            target: txt
                            color: "red"
                        }
                    }
                }
            }

            ColumnLayout {
                id: columnLayout
                spacing: 0
                Layout.fillWidth: true
                Layout.minimumWidth: 240
                Layout.preferredWidth: 240
                Layout.preferredHeight: 240

                Button {
                    id: button
                    text: qsTr("Add")
                }

                Button {
                    id: button1
                    text: qsTr("Refresh")
                }

                Button {
                    id: button2
                    text: qsTr("Remove")
                }
            }
        }

        Rectangle {
            id: rectangle1
            width: 200
            height: 200
            color: "#ffffff"
            Layout.row: 2
        }
    }

    Connections {
        target: dataToUI

        onWledDevicesSignal: {
            wledListModel.append(getWled)
        }

    }
}
