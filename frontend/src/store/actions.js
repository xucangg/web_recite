import { SET_INFO,SET_USER_SAVE_WORDS } from './mutation-types'

function makeAction (type) {
  return ({ commit }, ...args) => commit(type, ...args)
}


export const setInfo = makeAction(SET_INFO);
export const setUserSaveWords = makeAction(SET_USER_SAVE_WORDS)