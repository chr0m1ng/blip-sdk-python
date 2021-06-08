from lime_python import Command
from pytest import fixture, mark
from pytest_mock import MockerFixture
from src import WordSetExtension
from ....async_mock import async_return


class TestWordSetExtension:

    @fixture
    def target(self, mocker: MockerFixture) -> WordSetExtension:
        yield WordSetExtension(mocker.MagicMock())

    @mark.asyncio
    async def test_get_word_set_async(
        self,
        mocker: MockerFixture,
        target: WordSetExtension
    ) -> None:
        # Arrange
        word_set_id = '1234'
        expected_command = Command(
            'get',
            f'/word-sets/{word_set_id}?deep=True'
        )
        mock = mocker.MagicMock(
            return_value=async_return(None)
        )
        target.client.process_command_async = mock

        # Act
        await target.get_word_set_async(word_set_id, True)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_set_word_set_resource_async(
        self,
        mocker: MockerFixture,
        target: WordSetExtension
    ) -> None:
        # Arrange
        word_set_id = '1234'
        items = [
            {
                'name': 'nome'
            }
        ]
        word_set_resource = {
            'itemType': 'application/vnd.iris.ai.word+json',
            'items': items
        }
        expected_command = Command(
            'set',
            f'/word-sets/{word_set_id}',
            'application/vnd.lime.collection+json',
            word_set_resource
        )
        mock = mocker.MagicMock(
            return_value=async_return(None)
        )
        target.client.process_command_async = mock

        # Act
        await target.set_word_set_resource_async(word_set_id, items)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_set_word_set_async(
        self,
        mocker: MockerFixture,
        target: WordSetExtension
    ) -> None:
        # Arrange
        item = {
            'name': 'nome'
        }
        expected_command = Command(
            'set',
            '/word-sets',
            'application/vnd.iris.ai.word-set+json',
            item
        )
        mock = mocker.MagicMock(
            return_value=async_return(None)
        )
        target.client.process_command_async = mock

        # Act
        await target.set_word_set_async(item)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_analyse_word_set_async(
        self,
        mocker: MockerFixture,
        target: WordSetExtension
    ) -> None:
        # Arrange
        item = {
            'name': 'nome'
        }
        expected_command = Command(
            'set',
            '/word-sets-analysis',
            'application/vnd.iris.ai.word-set-analysis+json',
            item
        )
        mock = mocker.MagicMock(
            return_value=async_return(None)
        )
        target.client.process_command_async = mock

        # Act
        await target.analyse_word_set_async(item)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)

    @mark.asyncio
    async def test_delete_word_set_async(
        self,
        mocker: MockerFixture,
        target: WordSetExtension
    ) -> None:
        # Arrange
        word_set_id = '1234'
        expected_command = Command(
            'delete',
            f'/word-sets/{word_set_id}'
        )
        mock = mocker.MagicMock(
            return_value=async_return(None)
        )
        target.client.process_command_async = mock

        # Act
        await target.delete_word_set_async(word_set_id)

        # Assert
        expected_command.id = mock.call_args[0][0].id
        mock.assert_called_once_with(expected_command)